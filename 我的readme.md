改模型接口：
改 config.json 里的模型名 为你接口支持的模型
"judge" : { "model" : "deepseek-chat" , "min_score" : 0.5 } , "usecases" : { "per_day" : 5 , "model" : "deepseek-chat" , ... }

运行本项目：
python3 -m radar daily



## 日报不跑，需要单独跑的命令：
**1. 独立命令，daily 永远不包含，要单独跑**

| 命令 | 作用 | 花费 |
|---|---|---|
| `python -m radar pains "关键词"` | 一类工具的痛点缺口（Chrome 扩展差评、Reddit 抱怨、教程评论） | 约 $0.05/词 |
| `python -m radar keywords "名字"` | 给指定名字出关键词优先级表（usecases 的手动版） | 约 $0.05/名字 + $0.09/次 |
| `python -m radar leads` | 查看雷达已记下的线索和各信号命中率 | 免费 |

（`sources` 和 `mcp` 也算，但一个是 daily 的拆分版、一个是给 agent 用的服务器，不算缺内容。）

**2. daily 里的「周信号」，只有周一才自动跑，其他日子直接跳过（跳过时报告里连这一节都没有）**

默认 `weekday: 0`（周一），见 [config.py](file:///home/jk/new-term-radar/radar/config.py#L22-L29)。10-15 是周四，所以这 3 个全被跳了：

| 信号 | 手动触发 | 前提 |
|---|---|---|
| ③ 新站 new_sites | `--new-sites` | AIsa key（每查询约 $0.13） |
| ⑥ 收入 revenue | `--revenue` | TRUSTMRR_API_KEY |
| ⑦ 求助 asks | `--asks` | AIsa key（约 $0.12/次） |

```bash
python -m radar daily --new-sites --revenue --asks --out report.md
```

注意触发的是「今天就跑」，跑完后下次到周一还会照常跑。

**3. daily 会跑、但你当前环境跑不出来的部分**

- **⑥ revenue**：没配 `TRUSTMRR_API_KEY` 就没数据（需要在 TrustMRR 开发者后台生成）。
- **⑦ asks / 新词表 / 名字判断 / 复盘**：都要 AIsa 余额。你的 `2026-10-15 copy.md` 里名字判断报了 `HTTP 402 recharge_required`——余额不足时候选新词不排序、新词表直接报错，这部分跑不出结果。
- **⚡ 教程评论（tutorials）**：daily 会自动跑，但只在当天有 ⚡ 线索且配了 `GOANYAPI_API_KEY` 时才有输出。
- **④ Search Console（gsc）**：配置留 `{}` 就是关的，要先跑 `python scripts/gsc_auth.py gsc_client.json` 授权并填上 `gsc.site` 才会有内容。

总结：你 10-15 的报告没 Reddit 结果是正常的（周四 + 周信号跳过）；想看到 asks 就加 `--asks`，想看痛点就单独跑 `pains`，另外先把 AIsa 余额充上，否则名字判断和新词表都出不来。
# COMEXT Analysis Codex Showcase

This repository demonstrates how Codex with GPT-5.4 can coordinate a real data-analysis workflow through parallel subagents while keeping the lead agent focused on orchestration, review, and final assembly.

The concrete example is a Eurostat COMEXT energy-trade analysis. The workflow downloads monthly COMEXT archives for 2021-2025, prepares the data, computes energy and hydrocarbon trade summaries, and generates a Slidev presentation from separate report-writing tasks.

## What This Repo Showcases

- Parallel subagent execution for independent, bounded work.
- Clean separation between orchestration and implementation.
- Context management by moving large, repetitive, or exploratory tasks out of the lead agent thread.
- Review-and-assemble patterns where the lead agent validates subagent outputs before producing the final artifact.
- End-to-end automation from raw data acquisition to a running Slidev presentation.

## Why Subagents Are Useful Here

Subagents are a good fit when work can be split into clearly owned units. In this repo, Codex uses them in two places:

- Data acquisition: one subagent per year downloads COMEXT data for `2021`, `2022`, `2023`, `2024`, and `2025` in parallel.
- Report generation: four report-writing subagents produce separate chapter outputs for requirements, imports, exports, and Hungary.

This keeps the main agent context cleaner. The lead agent does not need to carry every download log, every chapter draft, and every intermediate decision in one growing context. Instead, it delegates bounded work, receives compact results, checks consistency, and assembles the final deck.

## Repository Workflow

The source of truth for execution is [AGENTS.md](AGENTS.md). It defines two phases.

### Phase 1: Acquire and Prepare COMEXT Data

1. Create `data/` if needed.
2. Download monthly COMEXT `.7z` archives for 2021-2025.
3. Normalize URL-encoded filenames.
4. Extract archives into yearly folders.
5. Remove archives only after successful extraction.

Raw data is stored under `data/` and should not be committed.

### Phase 2: Generate the Slidev Report

The report-generation phase is intentionally split into four subagent-owned outputs:

- `requirements-output.md`
- `imports-output.md`
- `exports-output.md`
- `hungary-output.md`

The lead agent reviews those files and concatenates them into `slides.md` in this order:

1. Requirements
2. Imports
3. Exports
4. Hungary

The generated report lives under a timestamped folder:

```text
reports/comext-analysis-v--<YYYYMMDD>-<HHMM>/
```

## Data Scope

The analysis uses Eurostat COMEXT `ext_go_detail`, with a focused SITC energy and hydrocarbons scope:

| SITC | Category |
| --- | --- |
| `32` | Coal, coke and briquettes |
| `33` | Petroleum, petroleum products and related materials |
| `34` | Gas, natural and manufactured |
| `35` | Electric current |

The workflow filters `PRODUCT_SITC` by prefix, so codes with more than two digits are included when they start with one of these categories.

## Generated Presentation

The Slidev deck is built from data-driven markdown and Vue/Chart.js components. The latest generated deck in this workspace is:

```text
reports/comext-analysis-v--20260423-1846/slides.md
```

To run that deck:

```bash
cd reports/comext-analysis-v--20260423-1846
npm install
npm run dev
```

Then open:

```text
http://localhost:3030/
```

## Important Files

| Path | Purpose |
| --- | --- |
| `AGENTS.md` | Full execution instructions for Codex agents |
| `download_data.sh` | Downloads all monthly COMEXT archives for one year |
| `fix_file_names.sh` | Normalizes URL-encoded downloaded filenames |
| `docs/comext_investigation.md` | Dataset notes and column reference |
| `scripts/aggregate_month.sh` | Aggregates one monthly file into SITC energy summaries |
| `scripts/build_slide_data.py` | Builds the JSON bundle used by the report |
| `scripts/init_slidev_report.py` | Initializes a Slidev report folder |
| `scripts/render_report_section.py` | Renders one report section output |

## Codex Pattern Demonstrated

This repo is not only a COMEXT analysis. It is a reproducible example of a Codex orchestration pattern:

1. The lead agent reads the execution contract.
2. Independent work is delegated to subagents.
3. Subagents produce bounded, named artifacts.
4. The lead agent reviews those artifacts.
5. The final report is assembled and run locally.

That pattern is useful when a task is too broad for one uninterrupted context but can be divided into clear units of ownership.

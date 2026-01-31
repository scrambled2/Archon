# Changelog

All notable changes to Archon are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.1-fork.1] - 2026-01-30 (scrambled2/Archon chris/stable)

### Added
- Hypercorn runner for MCP server with HTTP/2 support (`run_hypercorn.py`)
- FORK.md documenting fork-specific changes

### Fixed
- MCP server HTTP/2 streaming issues causing Claude Code timeouts (fixes #920)
- Recursive crawler relative URL resolution (urljoin for crawl4ai compatibility)

### Changed
- MCP Dockerfile now uses Hypercorn instead of Uvicorn
- Added `hypercorn[h2]>=0.16.0` to mcp dependencies

### Merged
- PR #928: Docker deployment improvements and async stability fixes

## [0.1.1] - 2026-01-23

### Added
- Changelog for release tracking

### Changed
- Version metadata bumped to 0.1.1 across backend, UI, and agent work orders
- README now shows the current release

---

[Unreleased]: https://github.com/AeyeOps/archon/compare/v0.1.1...HEAD
[0.1.1]: https://github.com/AeyeOps/archon/compare/v0.1.0...v0.1.1

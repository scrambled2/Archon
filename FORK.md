# Personal Fork: scrambled2/Archon

This is a personal fork of [coleam00/Archon](https://github.com/coleam00/Archon) with fixes for issues blocking Claude Code integration.

## Fork Details

| Attribute | Value |
|-----------|-------|
| **Fork** | https://github.com/scrambled2/Archon |
| **Upstream** | https://github.com/coleam00/Archon |
| **Branch** | `chris/stable` |
| **Base** | `upstream/main` (Nov 2025) |
| **Created** | 2026-01-30 |

## Changes from Upstream

### 1. Hypercorn HTTP/2 Fix (Issue #920)

The upstream MCP server uses Uvicorn which has HTTP/2 streaming issues, causing Claude Code's mcp-remote to timeout.

**Fix**: Replaced Uvicorn with Hypercorn for proper HTTP/2 support.

**Files changed**:
- `python/pyproject.toml` - Added `hypercorn[h2]>=0.16.0`
- `python/src/mcp_server/run_hypercorn.py` - NEW: Hypercorn runner
- `python/Dockerfile.mcp` - Changed entrypoint to run_hypercorn

### 2. Recursive Crawler URL Fix

crawl4ai sometimes returns relative URLs in `result.links["internal"]`, causing depth 2+ crawls to fail.

**Fix**: Added `urljoin` to resolve relative URLs before normalization.

**Files changed**:
- `python/src/server/services/crawling/strategies/recursive.py`

### 3. Merged PR #928

Docker deployment improvements and async stability fixes from upstream PR.

## Pulling Upstream Updates

```bash
# Fetch latest from upstream
git fetch upstream

# Merge into chris/stable
git checkout chris/stable
git merge upstream/main --no-edit

# Resolve any conflicts (likely in pyproject.toml)
# Then push and rebuild
git push origin chris/stable
docker compose build && docker compose up -d
```

## Verification

After deployment, verify the fixes are working:

```bash
# Check MCP logs for Hypercorn
docker logs archon-mcp --tail 10
# Should show: "Starting MCP server with Hypercorn (HTTP/2 enabled)"

# Test MCP endpoint
curl -X POST http://localhost:8051/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json, text/event-stream" \
  -d '{"jsonrpc":"2.0","method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1.0"}},"id":1}' \
  -s | head -c 200
# Should return event-stream response
```

## Related Issues

- [Issue #920](https://github.com/coleam00/Archon/issues/920) - MCP server doesn't work with mcp-remote
- [PR #928](https://github.com/coleam00/Archon/pull/928) - Docker deployment improvements

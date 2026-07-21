# Issue tracker: GitHub

Issues and planning artifacts live in GitHub Issues. Use `gh` from this clone so the repository is inferred from `origin`.

## Conventions

- Create: `gh issue create --title "..." --body "..."`
- Read: `gh issue view <number> --comments`
- List: `gh issue list --state open --json number,title,body,labels,assignees`
- Comment: `gh issue comment <number> --body "..."`
- Label or assign: `gh issue edit <number> --add-label "..."` / `--add-assignee @me`
- Close: `gh issue close <number> --comment "..."`

## Pull requests as a triage surface

No. External pull requests do not enter the issue-triage queue.

## Publishing

When a skill says to publish an issue, ticket, PRD, or spec, create a GitHub issue.

## Wayfinding operations

- Map: one issue labelled `wayfinder:map`.
- Ticket: a GitHub sub-issue labelled `wayfinder:research`, `wayfinder:prototype`, `wayfinder:grilling`, or `wayfinder:task`.
- If sub-issues are unavailable, add tickets to a map task list and put `Part of #<map>` in each ticket.
- Blocking: use GitHub native issue dependencies. If unavailable, put `Blocked by: #<number>` in the ticket body.
- Frontier: open, unblocked, unassigned child tickets in map order.
- Claim: assign the ticket to `@me` before work.
- Resolve: comment with the answer, close the ticket, then append its linked one-line gist to the map's Decisions so far.

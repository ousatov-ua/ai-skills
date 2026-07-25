# ast-grep — Structural Code Search & Rewrite (Agent Instructions)

ast-grep (`ast-grep`, alias `sg`) matches code by **AST structure**, not text.
It ignores formatting, comments, and string literals, and cannot produce
regex-style false positives on look-alike text.

Verify availability first: `ast-grep --version`. If missing, stop and say so —
do not silently fall back to text search for structural queries.

---

## 1. Tool Selection Policy (mandatory)

| Task | Tool | Forbidden |
|---|---|---|
| Find/replace a **code construct** (call, definition, import, class, method, pattern with args/body) | **ast-grep** | grep/ripgrep, text search |
| Find callers/callees of a function, incl. multiline or reformatted call sites | **ast-grep** | grep/ripgrep |
| Bulk structural rewrite (API migration, rename with semantics) | **ast-grep** `-r` | sed, manual edit loops |
| File/symbol overview of a large file (outline: imports, exports, definitions) | **ast-grep outline** | reading the whole file |
| Exact literal string, log message, TODO, comment, identifier in docs/config | text grep | ast-grep |
| Locate files by name/path | file glob | ast-grep, grep |
| Read a known file/line range to **understand** it | file read | ast-grep |

Rule of thumb: if the query is a *shape of code* → ast-grep.
If the query is a *string of text* → grep. If you already *know where* → read.

Never use grep to approximate a structural query ("find calls to X") — results
include comments, strings, and partial matches, and miss multiline forms.

---

## 2. Pattern Syntax (core)

Pattern = **valid code** with meta variables. It must parse in the target
language; invalid code is not a valid pattern.

| Syntax | Meaning |
|---|---|
| `$VAR` | any **single** named AST node (like regex `.`, but structural) |
| `$$$ARGS` | **zero or more** nodes (args, params, statements) |
| `$$VAR` | capture also unnamed nodes (operators, punctuation) |
| `$_VAR` | non-capturing wildcard (each occurrence independent) |
| same `$VAR` twice | both occurrences must be identical (`$A == $A`) |

Examples:

```
foo($A)                  # foo(...) with exactly one argument
foo($$$)                 # foo(...) with any arguments, incl. none/spread
console.log($$$ARGS)     # captures args into $ARGS for rewrite
function $F($$$P) { $$$ }# any function declaration
import $X from '$MOD'    # ES import
$A.await()               # method call named await on anything
```

Case matters: meta variables are `$UPPER_CASE`. `$camel` is literal code.

---

## 3. Commands

Binary is `ast-grep` or `sg`; `run` is the default subcommand.

### Search

```bash
ast-grep -p 'PATTERN' -l LANG [PATHS...]      # structural search
ast-grep -p 'PATTERN' --json=compact PATH      # machine-readable (prefer for parsing)
ast-grep -p 'PATTERN' -C 3 PATH                # context lines
ast-grep --kind KIND -l LANG PATH              # match by AST node kind
ast-grep -p 'PATTERN' --debug-query=ast -l LANG   # print pattern AST (debug)
```

`-l LANG` is required for stdin and for patterns without files; otherwise the
language is inferred from the file extension.

### Outline (file map instead of full read)

```bash
ast-grep outline PATH                          # symbols, imports, exports
ast-grep outline --type function,class PATH    # filtered
```

### Rewrite (search & replace)

```bash
ast-grep -p 'PATTERN' -r 'REPLACEMENT' PATH             # prints diff, asks
ast-grep -p 'PATTERN' -r 'REPLACEMENT' -U PATH          # apply all, no prompt
ast-grep -p 'PATTERN' -r 'REPLACEMENT' -i PATH          # interactive per-match
```

`$VAR`s captured in the pattern are substituted in the replacement.

### Rule-based scan (conditions beyond one pattern)

For *"X inside Y"*, *"X that has Z"*, *"X but not W"* use a YAML rule:

```bash
ast-grep scan --inline-rules '
id: my-rule
language: TypeScript
rule:
  pattern: Promise.all($A)
  has: { pattern: "await $_", stopBy: end }
' PATH
```

Rule anatomy: atomic (`pattern`, `kind`, `regex`) · relational (`inside`,
`has`, `follows`, `precedes`, with `stopBy: neighbor|end`) · composite
(`all`, `any`, `not`). All fields in one rule object are ANDed.

---

## 4. Workflow (always)

1. **Draft pattern** as real code from an actual usage site in the repo.
2. **Validate** it parses: run on one known file first, or
   `--debug-query=ast` if results look wrong.
3. **Scope narrow → wide**: one file → module → repo root. Check hit count
   before widening.
4. **Prefer `--json=compact`** when consuming output programmatically.
5. **Rewrites**: never use `-U` on first run. Run without `-U`, inspect the
   diff, then apply. Multi-file `-U` rewrites require explicit user approval.
6. After any rewrite, run the project's build/tests before claiming done.

---

## 5. Language IDs

Common `-l` values: `typescript` `tsx` `javascript` `python` `rust` `go`
`java` `kotlin` `c` `cpp` `csharp` `swift` `ruby` `php` `lua` `elixir`
`bash` `html` `css` `yaml` `json`. Full list: `ast-grep run --help`.

---

## 6. Pitfalls

- **Pattern must be valid code.** `foo($A,)` or `$OP` as an operator won't
  parse. Rewrite the snippet until it is real syntax.
- **One `$VAR` = one node.** `foo($A)` does not match `foo(a, b)` — use `$$$`.
- **Comments/strings never match.** This is a feature; do not "fix" patterns
  to chase comment text — that belongs to grep.
- **Quotes differ per language.** `'str'` is valid TS/Python, invalid in
  Rust/C/Java (use `"str"`).
- **Ambiguous snippet?** Give the pattern more surrounding context, or use a
  YAML rule with `kind`/`inside` instead of a bare pattern.
- **No match ≠ absence.** Confirm the language detection and that files are
  not ignored (`--no-ignore vcs` if searching gitignored paths intentionally).

---

## 7. Recipes

| Goal | Command sketch |
|---|---|
| All calls to `foo` with any args | `ast-grep -p 'foo($$$)' -l LANG .` |
| Calls where first arg is literal | `ast-grep -p 'foo("$_", $$$)' .` |
| Function definitions named `bar` | `ast-grep -p 'function bar($$$) { $$$ }' -l ts .` |
| Rust: `unwrap()` call sites | `ast-grep -p '$A.unwrap()' -l rust src/` |
| Python: class defs | `ast-grep -p 'class $C: $$$' -l python .` |
| Find `await` inside `Promise.all` | YAML rule: `pattern: Promise.all($A)` + `has` (see §3) |
| Rename method `old` → `new` on any receiver | `ast-grep -p '$A.old($$$)' -r '$A.new($$$)' src/` |
| Map of a big file before editing | `ast-grep outline path/to/file` |

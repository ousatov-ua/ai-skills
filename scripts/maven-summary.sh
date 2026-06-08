#!/usr/bin/env bash
set -u

log_file=${MAVEN_SUMMARY_LOG:-/tmp/maven-summary.log}

if [ "$#" -eq 0 ]; then
  set -- test
fi

mvn "$@" > "$log_file" 2>&1
status=$?

if command -v rg >/dev/null 2>&1; then
  rg -n "BUILD SUCCESS|BUILD FAILURE|Tests run:|Failures:|Errors:" "$log_file" || true
else
  grep -nE "BUILD SUCCESS|BUILD FAILURE|Tests run:|Failures:|Errors:" "$log_file" || true
fi

printf 'status=%s\n' "$status"
printf 'log=%s\n' "$log_file"
exit "$status"

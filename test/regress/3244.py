# Regression test for GitHub issue #3244 (Python-facing side):
# Journal.register_account crashed under --strict when called after
# parsing had finished, because journal_t::current_context is null
# outside of read() and the unknown-account warning dereferenced it.
# The warning now falls back to a location-free form instead.

import ledger

journal = ledger.session.read_journal_files()
xact = next(iter(journal))
post = xact[0]
print("about to call register_account", flush=True)
journal.register_account("Fresh:Unknown", post)
print("returned without crash", flush=True)

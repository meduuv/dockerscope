from collections.abc import Iterable, Mapping

def summarize(containers: Iterable[Mapping[str, object]]) -> dict[str, int]:
    """Count containers by lifecycle status."""
    result={}
    for c in containers:
        status=str(c.get("status","unknown")).strip().lower() or "unknown"
        result[status]=result.get(status,0)+1
    return dict(sorted(result.items()))

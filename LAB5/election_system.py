import hashlib
import secrets
from datetime import datetime
from xml.parsers.expat import ExpatError

from defusedxml.common import DefusedXmlException
from defusedxml.minidom import parseString

POLLS_CLOSE_HOUR = 18
voters = {}
ballots = []
candidates = ["Alice", "Bob", "NOTA"]


def register_voter(voter_id, name, age):
    """Register an eligible voter."""
    if not voter_id or not name or age < 18 or voter_id in voters:
        return False

    voters[voter_id] = {
        "name": name,
        "hash": hashlib.sha256(voter_id.encode()).hexdigest(),
        "voted": False,
    }
    return True


def is_officer(role):
    """Check whether a person has the election officer role."""
    return role == "election_officer"


def cast_vote(voter_id, candidate, when):
    """Record one valid vote before polls close."""
    if voter_id not in voters:
        return False

    if voters[voter_id]["voted"]:
        return False

    if candidate not in candidates:
        return False

    if when.hour >= POLLS_CLOSE_HOUR:
        return False

    ballots.append(candidate)
    voters[voter_id]["voted"] = True
    return True


def tally():
    """Count the votes for each candidate."""
    counts = {}
    for ballot in ballots:
        counts[ballot] = counts.get(ballot, 0) + 1
    return counts


def winner():
    """Return the candidate with the most votes."""
    counts = tally()
    if not counts:
        return None
    return max(counts, key=counts.get)


def vote_percent(name):
    """Return a candidate's percentage of all votes."""
    if not ballots:
        return 0
    return tally().get(name, 0) * 100 // len(ballots)


def turnout():
    """Return the percentage of registered voters who voted."""
    if not voters:
        return 0
    voted_count = sum(
        1 for voter in voters.values() if voter["voted"]
    )
    return voted_count * 100 // len(voters)


def count_for(candidate, ballot_list):
    """Count votes for a specific candidate."""
    return sum(1 for ballot in ballot_list if ballot == candidate)


def announce():
    """Create vote-count announcements for all candidates."""
    counts = tally()
    return [
        f"{name}: {counts.get(name, 0)}"
        for name in candidates
    ]


def receipt_number():
    """Generate a six-digit voting receipt number."""
    return f"RCPT-{secrets.randbelow(900000) + 100000}"


def import_postal_ballots(xml_text):
    """Import valid postal ballots using safe XML parsing."""
    try:
        document = parseString(xml_text)
    except (DefusedXmlException, ExpatError, TypeError, ValueError):
        return 0

    imported = 0

    for node in document.getElementsByTagName("ballot"):
        voter_id = node.getAttribute("voter")
        candidate = node.getAttribute("candidate")

        if voter_id not in voters:
            continue

        if voters[voter_id]["voted"] or candidate not in candidates:
            continue

        ballots.append(candidate)
        voters[voter_id]["voted"] = True
        imported += 1

    return imported


def main():
    print(
        "Register Asha (age 18):",
        register_voter("V1", "Asha", 18),
    )
    register_voter("V2", "Ben", 30)
    register_voter("V3", "Chen", 45)
    register_voter("V4", "Dia", 22)

    print("Is a plain 'voter' an election officer?", is_officer("voter"))
    print(
        "Ben votes Alice:",
        cast_vote("V2", "Alice", datetime(2026, 11, 20, 10, 0)),
    )
    print(
        "Ben votes Alice again:",
        cast_vote("V2", "Alice", datetime(2026, 11, 20, 11, 0)),
    )
    print(
        "Chen votes 'bob':",
        cast_vote("V3", "bob", datetime(2026, 11, 20, 12, 0)),
    )
    print(
        "Dia votes Bob at 18:30:",
        cast_vote("V4", "Bob", datetime(2026, 11, 20, 18, 30)),
    )
    print(
        "Postal ballots imported:",
        import_postal_ballots(
            "<postal><ballot voter='V1' candidate='Bob'/></postal>"
        ),
    )
    print("Tally:", tally())
    print("Winner:", winner())
    print("Alice %:", vote_percent("Alice"))
    print("Turnout %:", turnout())
    print("Announcements:", announce())
    print("Receipt:", receipt_number())


if __name__ == "__main__":
    main()

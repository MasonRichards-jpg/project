# ── In-memory data store (replace with a real DB later) ───────────────────────

trip = {
    'name': 'Bali 2025',
    'destination': 'Bali, Indonesia',
    'start_date': '2025-06-12',
    'end_date': '2025-06-22',
    'currency': 'USD',
    'cover': '🌴',
    'description': '10-day group vacation to Bali.',
    'budget': 4000.00,
    'split_method': 'equal',
    'members': ['Alex', 'Sara', 'Mike', 'Jess', 'Leo'],
}

expenses = []       # list of expense dicts
settlements = []    # list of settled debt dicts


# ── Expenses ──────────────────────────────────────────────────────────────────

def get_expenses(sort=None, search=None, cat_filter=None, page=1):
    """Return filtered, sorted, paginated list of expenses."""
    pass

def add_expense(description, amount, date, paid_by, category, split, notes=''):
    """Create a new expense and append it to the expenses list."""
    pass

def get_expense(expense_id):
    """Return a single expense by its ID, or None if not found."""
    pass

def update_expense(expense_id, **fields):
    """Update fields on an existing expense."""
    pass

def delete_expense(expense_id):
    """Remove an expense by ID. Returns True on success."""
    pass

def export_csv():
    """Return expenses as a CSV string for download."""
    pass


# ── Trip ──────────────────────────────────────────────────────────────────────

def get_trip():
    """Return the current trip dict."""
    return trip

def save_trip(trip_name, destination, start_date, end_date,
              currency, cover, description, budget, split_method):
    """Overwrite trip fields with new values. Members are managed separately."""
    global trip
    trip.update({
        'name': trip_name,
        'destination': destination,
        'start_date': start_date,
        'end_date': end_date,
        'currency': currency,
        'cover': cover,
        'description': description,
        'budget': float(str(budget).replace(',', '')),
        'split_method': split_method,
    })
    

def create_new_trip():
    """Reset the trip and expenses to defaults for a fresh trip."""
    pass

def reset_expenses():
    """Clear all expenses without deleting the trip."""
    pass

def delete_trip():
    """Delete the current trip and all associated expenses."""
    pass


# ── Members ───────────────────────────────────────────────────────────────────

def add_member(name_or_email):
    """Add a new member to the trip's member list."""
    pass

def remove_member(name):
    """Remove a member from the trip by name."""
    pass


# ── Balances ──────────────────────────────────────────────────────────────────

def get_balances(member=None):
    """
    Calculate how much each member paid vs. their fair share.
    If member is given, filter the transaction log to that member.
    Returns a dict with member stats and a list of who-owes-who debts.
    """
    pass


# ── Settle Up ─────────────────────────────────────────────────────────────────

def get_settlements():
    """Return all pending and completed settlements."""
    return settlements

def settle_debt(debtor, creditor):
    """Mark the debt from debtor → creditor as settled."""
    pass

def mark_all_settled():
    """Mark every pending debt as settled."""
    pass

def send_reminder(debtor):
    """Send a reminder notification to the debtor (email / push / etc.)."""
    pass

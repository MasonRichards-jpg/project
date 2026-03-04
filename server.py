from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import main

app = Flask(__name__)

@app.template_filter('fmtdate')
def fmtdate(value):
    try:
        return datetime.strptime(value, '%Y-%m-%d').strftime('%b %d')
    except Exception:
        return value


# ── Overview ──────────────────────────────────────────────────────────────────

@app.route('/')
@app.route('/index')
def index():
    trip = main.get_trip()
    balances = main.get_balances()
    recent_expenses = main.get_expenses()
    return render_template('index.html', trip=trip, balances=balances, expenses=recent_expenses)


# ── Expenses ──────────────────────────────────────────────────────────────────

@app.route('/expenses')
def expenses():
    sort       = request.args.get('sort', 'newest')
    search     = request.args.get('search', '')
    cat_filter = request.args.get('cat_filter', 'all')
    page       = int(request.args.get('page', 1))
    expense_list = main.get_expenses(sort=sort, search=search, cat_filter=cat_filter, page=page)
    return render_template('expenses.html', expenses=expense_list, trip=main.get_trip())

@app.route('/expenses/add', methods=['POST'])
def expenses_add():
    main.add_expense(
        description = request.form['description'],
        amount      = request.form['amount'],
        date        = request.form['date'],
        paid_by     = request.form['paid_by'],
        category    = request.form['category'],
        split       = request.form.getlist('split'),
        notes       = request.form.get('notes', ''),
    )
    return redirect(url_for('expenses'))

@app.route('/expenses/export')
def expenses_export():
    # TODO: return main.export_csv() as a file download using flask.Response
    return redirect(url_for('expenses'))

@app.route('/expenses/<int:expense_id>/edit')
def expenses_edit(expense_id):
    expense = main.get_expense(expense_id)
    return render_template('expenses.html', editing=expense, trip=main.get_trip())

@app.route('/expenses/<int:expense_id>/delete', methods=['POST'])
def expenses_delete(expense_id):
    main.delete_expense(expense_id)
    return redirect(url_for('expenses'))


# ── Balances ──────────────────────────────────────────────────────────────────

@app.route('/balances')
def balances():
    member = request.args.get('member', 'all')
    balance_data = main.get_balances(member=member)
    return render_template('balances.html', balances=balance_data, trip=main.get_trip())


# ── Settle Up ─────────────────────────────────────────────────────────────────

@app.route('/settle-up')
def settle_up():
    settlements = main.get_settlements()
    return render_template('settle-up.html', settlements=settlements, trip=main.get_trip())

@app.route('/settle-up/mark-all', methods=['POST'])
def settle_up_mark_all():
    main.mark_all_settled()
    return redirect(url_for('settle_up'))

@app.route('/settle-up/remind', methods=['POST'])
def settle_up_remind():
    main.send_reminder(debtor=request.form['debtor'])
    return redirect(url_for('settle_up'))

@app.route('/settle-up/settle', methods=['POST'])
def settle_up_settle():
    main.settle_debt(
        debtor   = request.form['debtor'],
        creditor = request.form['creditor'],
    )
    return redirect(url_for('settle_up'))

@app.route('/settle-up/history')
def settle_up_history():
    settlements = main.get_settlements()
    return render_template('settle-up.html', settlements=settlements, trip=main.get_trip())


# ── Trip ──────────────────────────────────────────────────────────────────────

@app.route('/trip')
def trip():
    trip_data = main.get_trip()
    return render_template('trip.html', trip=trip_data)

@app.route('/trip/save', methods=['POST'])
def trip_save():
    main.save_trip(
        trip_name    = request.form['trip_name'],
        destination  = request.form['destination'],
        start_date   = request.form['start_date'],
        end_date     = request.form['end_date'],
        currency     = request.form['currency'],
        cover        = request.form['cover'],
        description  = request.form['description'],
        budget       = request.form['budget'],
        split_method = request.form['split_method'],
    )
    return redirect(url_for('trip'))

@app.route('/trip/new', methods=['POST'])
def trip_new():
    main.create_new_trip()
    return redirect(url_for('trip'))

@app.route('/trip/add-member', methods=['POST'])
def trip_add_member():
    main.add_member(request.form['member'])
    return redirect(url_for('trip'))

@app.route('/trip/remove-member', methods=['POST'])
def trip_remove_member():
    main.remove_member(request.form['member'])
    return redirect(url_for('trip'))

@app.route('/trip/reset', methods=['POST'])
def trip_reset():
    main.reset_expenses()
    return redirect(url_for('trip'))

@app.route('/trip/delete', methods=['POST'])
def trip_delete():
    main.delete_trip()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

# L04 Your First Workflow: Sheets In, Sheets Out

Course: AI-16 · Module: M1 · Objectives: O3 · Video: 5 min (screen demo)

## Hook
Many small businesses already run on a spreadsheet. If your automation can read a sheet, change the data and write it back, you can automate real work before you add any AI at all.

## Explanation
In this course Google Sheets is our simple database. A workflow that uses it has three parts:

1. **Read.** A Google Sheets node reads rows. Each row becomes one **item** in n8n, with the column headers as field names.
2. **Change.** An **Edit Fields (Set)** node, an **IF** node or a **Code** node changes or adds fields on each item. [VERSION]
3. **Write.** A second Google Sheets node updates the rows or adds new ones.

n8n processes items one by one through most nodes. If 15 rows come in, 15 items go out, and each node runs its settings for every item.

**Credentials first.** n8n needs permission to use your Google account. In the self-hosted version this usually means creating an OAuth client in a Google Cloud project, turning on the Google Sheets API (and the Google Drive API to list files), and pasting the client ID and secret into an n8n credential. The steps in the Google Cloud console change often, so follow the current n8n documentation for Google credentials. [VERSION] Use a test Google account or a test folder, and only give access to the sheets you need.

To update rows, the node needs a column that identifies each row, such as `order_id`. It uses this column to match an item to the right row. [VERSION]

**Analogy:** The workflow is like a clerk with a clipboard. The clerk copies rows from the ledger to the clipboard (read), writes a note next to each row (change), and then copies the notes back into the right lines of the ledger by checking the order number (write). If the order numbers are missing, the clerk cannot find the right line.

For simple rules, a Code node is short and clear. This JavaScript runs once for all items:

```javascript
const LIMIT = 5000;
return $input.all().map(item => {
  item.json.flag = item.json.amount > LIMIT ? 'check' : 'ok';
  return item;
});
```

## Worked Example
Wanjiru Kamau runs a hypothetical bakery in Nairobi, Kenya. She wants to phone every customer who orders more than 5,000 Kenyan shillings, to confirm the order before baking. She uses sample data only. On screen, she:

1. Creates a Google Sheet called "orders" with columns `order_id`, `customer`, `item`, `amount` and `flag`, and 15 rows of invented orders.
2. In n8n, creates a credential for Google Sheets using the current OAuth steps and tests that it connects. [VERSION]
3. Adds a **Manual Trigger**, then a **Google Sheets** node with the operation to get rows, and selects the "orders" document and sheet. [VERSION]
4. Runs the node: the output shows 15 items.
5. Adds a **Code** node with the script above. The output shows `flag` set to "check" on 4 items and "ok" on the rest.
6. Adds a second **Google Sheets** node with the operation to update rows, sets "column to match on" to `order_id`, and maps the `flag` field. [VERSION]
7. Runs the whole workflow and opens the sheet: the flag column is now filled.

She then notices that one amount was typed as text ("6,200"), so the comparison failed. She adds `Number(String(item.json.amount).replace(/,/g, ''))` to clean the value. Real data is always less tidy than you expect.

## Common Mistake
Learners often use the "append" operation when they mean "update". The workflow runs without an error, but it adds 15 new rows to the bottom of the sheet instead of filling the flag column. Before writing, decide: am I adding new records or changing existing ones? For changes, use the update operation with a unique ID column to match on.

## Key Takeaways
1. A Sheets workflow reads rows as items, changes them with Set, IF or Code nodes, and writes them back.
2. Updating rows needs a unique ID column to match on; appending adds new rows instead.
3. Set up the Google credential with the current documentation and give it access to test data only.

## Hands-on Exercise
**Task:** Build a workflow that reads an "orders" sheet, marks orders above a threshold as "check", and writes the flag to a new column.
**Tools:** Google Sheets (free Google account); n8n self-hosted.
**Steps:**
1. Create a sheet "orders" with columns `order_id`, `customer`, `item`, `amount`, `flag` and 15 rows of invented sample data. Do not use real customer names or phone numbers. [REGION]
2. Create a Google Sheets credential in n8n, following the current documentation. [VERSION]
3. Build: Manual Trigger, Google Sheets (get rows), Code (set `flag`), Google Sheets (update rows, match on `order_id`).
4. Choose your own threshold and put it in a constant at the top of the Code node.
5. Run the workflow and check the sheet.
6. Add one messy row (an amount written as text) and make the workflow handle it.
**What good looks like:** All 15 rows have a correct flag, no duplicate rows were added, the threshold is easy to change, and the messy row is handled without an error.
**Time:** about 40 minutes

## Review Flags
- [VERSION] Google Cloud OAuth client setup, the APIs to enable, and the n8n Google Sheets node operations ("get rows", "update row", "column to match on") change often and must be checked before recording.
- [VERSION] n8n node names (Edit Fields (Set), IF, Code) and the Code node's `$input.all()` syntax must be confirmed for the current release.
- [REGION] Use invented sample data only; storing real customer names or phone numbers in a sheet may be restricted by local data protection law.

# L04 Your First Workflow: Sheets In, Sheets Out | Presenter Script

Course: AI-16 · Video: 5 min · Words: 684

## Hook
Many small businesses already run on a spreadsheet. If your automation can read a sheet, change the data, and write it back, you can automate real work before you add any AI at all.

## Explain
Last time, you installed n8n. Now let's connect it to real data. In this course, Google Sheets is our simple database, and a workflow that uses it has three parts.

First, read. A Google Sheets node reads rows, and each row becomes one item in n8n, with the column headers as field names. Second, change. A Set, IF or Code node adds or changes fields on each item. Third, write. A second Sheets node updates the rows, or adds new ones.

Most nodes handle items one by one. If fifteen rows come in, fifteen items go out, and each node runs its settings for every item.

Before any of this, n8n needs permission to use your Google account. You create a credential. In the self-hosted version, this usually means setting up a Google Cloud project and turning on the Sheets API. The steps change often, so follow the current n8n guide. And use a test account, with access only to the sheets you need.

Here is a way to picture it. The workflow is like a clerk with a clipboard. The clerk copies rows from the ledger, writes a note next to each one, then copies the notes back into the right lines of the ledger, by checking the order number.

If the order numbers are missing, the clerk cannot find the right line. That is why updates need a column that identifies each row, such as an order ID.

## Demonstrate
Let's build it. Wanjiru Kamau runs a bakery in Nairobi, Kenya. She wants to phone every customer who orders more than five thousand Kenyan shillings, to confirm before baking. She uses sample data only. First, she creates a sheet called orders, with fifteen invented rows.

In n8n, she creates a Google Sheets credential using the current steps, and tests that it connects. Then she adds a manual trigger, and a Sheets node that gets rows from the orders sheet. When she runs it, the output shows fifteen items.

Next, she adds a Code node. For a simple rule like this, a few lines of code are short and clear. The code sets a limit of five thousand at the top. Then, for every item, it sets the flag to check if the amount is above the limit, and to ok if not. You'll see something like four items marked check, and the rest marked ok.

To write back, she adds a second Sheets node, with the update operation. She sets the column to match on to the order ID, and maps the flag field. She runs the whole workflow, opens the sheet, and the flag column is filled.

Then she notices a problem. One amount was typed as text, with a comma, so the comparison failed. She adds a small step to remove the comma and turn it into a number. Real data is always less tidy than you expect.

A common mistake is to use append when you mean update. The workflow runs without an error, but it adds fifteen new rows at the bottom, instead of filling the flag column. So before you write, ask: am I adding new records, or changing existing ones? For changes, use update, with a unique ID column to match on.

## Recap
Let's recap. First, a Sheets workflow reads rows as items, changes them with Set, IF or Code nodes, and writes them back. Second, updating rows needs a unique ID column to match on. Appending adds new rows instead. Third, set up the Google credential with the current guide, and give it access to test data only.

## CTA
Now it is your turn. In the exercise below this video, you will build the same orders workflow with your own threshold, then add one messy row and make the workflow handle it. It takes about forty minutes. In the next lesson, we add AI, with Calling the Claude API from n8n. See you there.

## Thumbnail
Headline: Sheets In, Sheets Out
Image: Navy background, a spreadsheet grid flowing into an n8n-style node and back into the grid with a new teal 'check' column, headline in teal Inter Bold.

## Production Notes
- [VERSION] Google Cloud OAuth client setup, the APIs to enable, and the n8n Google Sheets node operations ('get rows', 'update row', 'column to match on') change often and must be checked before recording.
- [VERSION] n8n node names (Edit Fields (Set), IF, Code) and the Code node's $input.all() syntax must be confirmed for the current release.
- [REGION] Use invented sample data only; storing real customer names or phone numbers in a sheet may be restricted by local data protection law. The demo sheet contains only invented names and no phone numbers.
- Screen recording: use a test Google account. Blur the OAuth client ID and secret. The Code node shows the JavaScript from content.md; the voiceover describes it and does not read it.
- Wanjiru Kamau and her Nairobi bakery are fictional.

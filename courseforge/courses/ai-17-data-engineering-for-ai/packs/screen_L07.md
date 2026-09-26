# Screen Demo Pack: AI-17 L07 Sources, Staging Models and ref()

Record with OBS Studio at 1920×1080, 30 fps. Record the screen only, with no microphone: the presenter's HeyGen audio is laid over it in the edit.
Before recording: close notifications, hide bookmarks and personal accounts, use sample data only, and zoom the browser or editor so text is readable on a phone.
Pace each clip to the narration shown. It can run a little long, because the editor trims it. Upload each clip to `/incoming/` with the exact filename.

## Clip 1: scene 8

- **Filename:** `ai-17-data-engineering-for-ai_L07_screen_1.mp4`
- **Target length:** about 12 seconds

**Steps**

1. Create the folder models/staging/
2. Create models/staging/_sources.yml
3. Type the YAML from content.md: version 2, source raw, schema raw, table orders

**Narration over this clip (for pacing)**

> First, he creates a staging folder, and a sources file inside it. The file declares one source called raw, in the raw schema, with one table: orders.

## Clip 2: scene 9

- **Filename:** `ai-17-data-engineering-for-ai_L07_screen_2.mp4`
- **Target length:** about 19 seconds

**Steps**

1. Create models/staging/stg_orders.sql
2. Type the source CTE: select distinct * from {{ source('raw', 'orders') }}
3. Type the casts for order_id, order_date and amount_usd, as in content.md

**Narration over this clip (for pacing)**

> Next, the staging model. It reads the source with the source function, and keeps only distinct rows. Then it casts the order ID to a whole number, the date to a real date, and the amount to a decimal, turning empty text into null.

## Clip 3: scene 10

- **Filename:** `ai-17-data-engineering-for-ai_L07_screen_3.mp4`
- **Target length:** about 14 seconds

**Steps**

1. Type: lower(trim(status)) as order_status, upper(country) as country_code
2. Type: where customer_id <> 'TEST'
3. Highlight the new column names amount_usd, order_status, country_code

**Narration over this clip (for pacing)**

> It lowercases and trims the status, uppercases the country code, and removes the test customer. Notice the names: lowercase with underscores, the unit in the amount name, and a clear suffix for codes.

## Clip 4: scene 11

- **Filename:** `ai-17-data-engineering-for-ai_L07_screen_4.mp4`
- **Target length:** about 10 seconds

**Steps**

1. Delete models/orders_first.sql
2. Run: dbt run --select stg_orders
3. Highlight the success line in the log

**Narration over this clip (for pacing)**

> He deletes the first model from last lesson, because staging replaces it. Then he runs only the staging model, and the log shows success.

## Clip 5: scene 12

- **Filename:** `ai-17-data-engineering-for-ai_L07_screen_5.mp4`
- **Target length:** about 26 seconds

**Steps**

1. Run: select * from main.stg_orders order by order_id;
2. Show 7 rows; highlight order 1005 status 'delivered' and order 1006 amount_usd NULL
3. Caption: 9 raw rows → 7 staged rows

**Narration over this clip (for pacing)**

> He queries the result. Seven rows from nine: the duplicate of order ten o seven and the test row are gone. Order ten o five now says delivered in lowercase. And order ten o six still has a null amount. Sipho keeps it, because a missing amount is a fact about the data, and a test will report it later.

## Production notes for this lesson

- [VERSION] dbt YAML source syntax, the source() and ref() functions and the default schema name for query results (main with dbt-duckdb) must be checked against the current dbt Core release and adapter.
- Screen output must match content.md: 7 rows from the 9 raw rows; order_id INTEGER, order_date DATE, amount_usd DECIMAL(10,2); order 1005 status 'delivered'; order 1006 amount NULL.
- Sipho and the craft marketplace in Durban, South Africa are fictional; the orders file is the course sample from L03.

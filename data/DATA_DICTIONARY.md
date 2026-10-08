# NordCart – Data Dictionary

NordCart is a (fictional) online shop selling to customers in Germany and neighbouring countries.
The export covers **July 2024 – June 2026**. All money values are in EUR.

## customers.csv
| Column | Meaning |
|---|---|
| customer_id | Unique customer ID |
| signup_date | Date the customer created an account |
| country | Customer country |
| age | Age at signup |
| segment | Marketing segment (Student, Professional, Family, Senior) |
| acquisition_channel | Channel through which the customer first found us |
| newsletter_opt_in | Customer agreed to receive the newsletter |
| favorite_color | From the onboarding survey |
| zodiac_sign | From the onboarding survey |
| preferred_language | Website language |

## products.csv
| Column | Meaning |
|---|---|
| product_id | Unique product ID |
| product_name | Internal product name |
| category | Product category |
| supplier_id | Supplier who delivers the product |
| price_eur | Current list price |
| unit_cost_eur | What we pay the supplier per unit |
| weight_g | Shipping weight in grams |
| color | Product colour |
| launch_date | Date the product was added to the shop |

## orders.csv
| Column | Meaning |
|---|---|
| order_id | Unique order ID |
| customer_id | Customer who placed the order |
| order_date | Date of the order |
| campaign_id | Marketing campaign the order is attributed to (empty = no campaign) |
| payment_method | Payment method used |
| device | Device used to place the order |
| browser | Browser used |
| status | completed / returned / cancelled |
| shipping_country | Delivery country |
| total_amount | Order value |
| currency | Currency |

## order_items.csv
| Column | Meaning |
|---|---|
| order_id | Order the line belongs to |
| product_id | Product bought |
| quantity | Number of units |
| unit_price_eur | List price per unit at time of order |
| discount_pct | |

## campaigns.csv
| Column | Meaning |
|---|---|
| campaign_id | Unique campaign ID |
| campaign_name | Campaign name |
| channel | Marketing channel |
| start_date / end_date | Campaign period |
| budget_eur | Total campaign spend |

## support_tickets.csv
| Column | Meaning |
|---|---|
| ticket_id | Unique ticket ID |
| customer_id | Customer who contacted support |
| order_id | Related order |
| created_at | When the ticket was opened |
| topic | Reason for contact |
| channel | email / chat / phone |
| resolution_hours | Time until the ticket was closed |
| satisfaction_score | Customer rating after resolution (scale 1–5) |

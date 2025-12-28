-- Jobber Data Schema for Supabase
-- Run this in Supabase Studio SQL Editor after enabling pgvector
--
-- Schema design:
-- - Each table stores the full Jobber API response in `data` JSONB column
-- - Key fields are extracted for efficient querying
-- - `embedding` column (vector) added for AI semantic search
-- - Upsert-friendly with unique constraint on jobber_id

-- Enable pgvector if not already done
CREATE EXTENSION IF NOT EXISTS vector;

-- =============================================================================
-- SYNC LOG - Track sync operations
-- =============================================================================
CREATE TABLE IF NOT EXISTS jobber_sync_log (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    entity_type TEXT NOT NULL,
    sync_started_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    sync_completed_at TIMESTAMPTZ,
    records_synced INTEGER DEFAULT 0,
    records_failed INTEGER DEFAULT 0,
    status TEXT NOT NULL DEFAULT 'running', -- running, completed, failed
    error_message TEXT,
    last_jobber_updated_at TIMESTAMPTZ, -- For incremental sync
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_sync_log_entity_type ON jobber_sync_log(entity_type);
CREATE INDEX IF NOT EXISTS idx_sync_log_status ON jobber_sync_log(status);

-- =============================================================================
-- USERS - Team members
-- =============================================================================
CREATE TABLE IF NOT EXISTS jobber_users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    jobber_id TEXT NOT NULL UNIQUE,

    -- Extracted fields for querying
    email TEXT,
    name TEXT,
    role TEXT,
    is_active BOOLEAN DEFAULT true,

    -- Full API response
    data JSONB NOT NULL,

    -- Metadata
    synced_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_users_jobber_id ON jobber_users(jobber_id);
CREATE INDEX IF NOT EXISTS idx_users_email ON jobber_users(email);

-- =============================================================================
-- CLIENTS - Customer records
-- =============================================================================
CREATE TABLE IF NOT EXISTS jobber_clients (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    jobber_id TEXT NOT NULL UNIQUE,

    -- Extracted fields for querying
    name TEXT,
    first_name TEXT,
    last_name TEXT,
    company_name TEXT,
    email TEXT,
    phone TEXT,
    billing_address JSONB,
    tags TEXT[],
    is_lead BOOLEAN DEFAULT false,
    is_archived BOOLEAN DEFAULT false,

    -- Full API response
    data JSONB NOT NULL,

    -- Vector embedding for AI search
    embedding vector(1536),

    -- Metadata
    synced_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_clients_jobber_id ON jobber_clients(jobber_id);
CREATE INDEX IF NOT EXISTS idx_clients_email ON jobber_clients(email);
CREATE INDEX IF NOT EXISTS idx_clients_name ON jobber_clients(name);
CREATE INDEX IF NOT EXISTS idx_clients_company ON jobber_clients(company_name);
CREATE INDEX IF NOT EXISTS idx_clients_tags ON jobber_clients USING GIN(tags);

-- =============================================================================
-- PROPERTIES - Service locations
-- =============================================================================
CREATE TABLE IF NOT EXISTS jobber_properties (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    jobber_id TEXT NOT NULL UNIQUE,

    -- Extracted fields for querying
    client_jobber_id TEXT, -- Reference to client
    address_line1 TEXT,
    address_line2 TEXT,
    city TEXT,
    state TEXT,
    postal_code TEXT,
    country TEXT,
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8),

    -- Full API response
    data JSONB NOT NULL,

    -- Metadata
    synced_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_properties_jobber_id ON jobber_properties(jobber_id);
CREATE INDEX IF NOT EXISTS idx_properties_client ON jobber_properties(client_jobber_id);
CREATE INDEX IF NOT EXISTS idx_properties_city ON jobber_properties(city);
CREATE INDEX IF NOT EXISTS idx_properties_postal ON jobber_properties(postal_code);

-- =============================================================================
-- JOBS - Work orders
-- =============================================================================
CREATE TABLE IF NOT EXISTS jobber_jobs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    jobber_id TEXT NOT NULL UNIQUE,

    -- Extracted fields for querying
    job_number TEXT,
    title TEXT,
    description TEXT,
    status TEXT, -- draft, active, completed, archived
    job_type TEXT,
    client_jobber_id TEXT,
    property_jobber_id TEXT,
    assigned_user_ids TEXT[],
    total DECIMAL(12, 2),

    -- Dates
    start_date DATE,
    end_date DATE,
    completed_at TIMESTAMPTZ,

    -- Full API response
    data JSONB NOT NULL,

    -- Vector embedding for AI search
    embedding vector(1536),

    -- Metadata
    synced_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_jobs_jobber_id ON jobber_jobs(jobber_id);
CREATE INDEX IF NOT EXISTS idx_jobs_number ON jobber_jobs(job_number);
CREATE INDEX IF NOT EXISTS idx_jobs_status ON jobber_jobs(status);
CREATE INDEX IF NOT EXISTS idx_jobs_client ON jobber_jobs(client_jobber_id);
CREATE INDEX IF NOT EXISTS idx_jobs_property ON jobber_jobs(property_jobber_id);
CREATE INDEX IF NOT EXISTS idx_jobs_start_date ON jobber_jobs(start_date);

-- =============================================================================
-- VISITS - Scheduled appointments
-- =============================================================================
CREATE TABLE IF NOT EXISTS jobber_visits (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    jobber_id TEXT NOT NULL UNIQUE,

    -- Extracted fields for querying
    job_jobber_id TEXT,
    title TEXT,
    status TEXT, -- scheduled, in_progress, completed, cancelled
    scheduled_start TIMESTAMPTZ,
    scheduled_end TIMESTAMPTZ,
    actual_start TIMESTAMPTZ,
    actual_end TIMESTAMPTZ,
    assigned_user_ids TEXT[],

    -- Full API response
    data JSONB NOT NULL,

    -- Metadata
    synced_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_visits_jobber_id ON jobber_visits(jobber_id);
CREATE INDEX IF NOT EXISTS idx_visits_job ON jobber_visits(job_jobber_id);
CREATE INDEX IF NOT EXISTS idx_visits_status ON jobber_visits(status);
CREATE INDEX IF NOT EXISTS idx_visits_scheduled ON jobber_visits(scheduled_start);

-- =============================================================================
-- QUOTES - Estimates
-- =============================================================================
CREATE TABLE IF NOT EXISTS jobber_quotes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    jobber_id TEXT NOT NULL UNIQUE,

    -- Extracted fields for querying
    quote_number TEXT,
    title TEXT,
    status TEXT, -- draft, sent, approved, declined, converted, archived
    client_jobber_id TEXT,
    property_jobber_id TEXT,
    subtotal DECIMAL(12, 2),
    tax DECIMAL(12, 2),
    total DECIMAL(12, 2),

    -- Dates
    sent_at TIMESTAMPTZ,
    valid_until DATE,
    approved_at TIMESTAMPTZ,

    -- Full API response
    data JSONB NOT NULL,

    -- Metadata
    synced_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_quotes_jobber_id ON jobber_quotes(jobber_id);
CREATE INDEX IF NOT EXISTS idx_quotes_number ON jobber_quotes(quote_number);
CREATE INDEX IF NOT EXISTS idx_quotes_status ON jobber_quotes(status);
CREATE INDEX IF NOT EXISTS idx_quotes_client ON jobber_quotes(client_jobber_id);

-- =============================================================================
-- INVOICES - Billing records
-- =============================================================================
CREATE TABLE IF NOT EXISTS jobber_invoices (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    jobber_id TEXT NOT NULL UNIQUE,

    -- Extracted fields for querying
    invoice_number TEXT,
    status TEXT, -- draft, sent, partial, paid, bad_debt, archived
    client_jobber_id TEXT,
    job_jobber_id TEXT,
    subtotal DECIMAL(12, 2),
    tax DECIMAL(12, 2),
    total DECIMAL(12, 2),
    amount_due DECIMAL(12, 2),

    -- Dates
    issued_at TIMESTAMPTZ,
    due_date DATE,
    paid_at TIMESTAMPTZ,

    -- Full API response
    data JSONB NOT NULL,

    -- Metadata
    synced_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_invoices_jobber_id ON jobber_invoices(jobber_id);
CREATE INDEX IF NOT EXISTS idx_invoices_number ON jobber_invoices(invoice_number);
CREATE INDEX IF NOT EXISTS idx_invoices_status ON jobber_invoices(status);
CREATE INDEX IF NOT EXISTS idx_invoices_client ON jobber_invoices(client_jobber_id);
CREATE INDEX IF NOT EXISTS idx_invoices_job ON jobber_invoices(job_jobber_id);
CREATE INDEX IF NOT EXISTS idx_invoices_due ON jobber_invoices(due_date);

-- =============================================================================
-- LINE ITEMS - Items on quotes/invoices
-- =============================================================================
CREATE TABLE IF NOT EXISTS jobber_line_items (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    jobber_id TEXT NOT NULL UNIQUE,

    -- Extracted fields for querying
    parent_type TEXT, -- quote, invoice, job
    parent_jobber_id TEXT,
    name TEXT,
    description TEXT,
    quantity DECIMAL(12, 4),
    unit_price DECIMAL(12, 2),
    total DECIMAL(12, 2),

    -- Full API response
    data JSONB NOT NULL,

    -- Metadata
    synced_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_line_items_jobber_id ON jobber_line_items(jobber_id);
CREATE INDEX IF NOT EXISTS idx_line_items_parent ON jobber_line_items(parent_type, parent_jobber_id);

-- =============================================================================
-- PAYMENTS - Payment records
-- =============================================================================
CREATE TABLE IF NOT EXISTS jobber_payments (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    jobber_id TEXT NOT NULL UNIQUE,

    -- Extracted fields for querying
    invoice_jobber_id TEXT,
    client_jobber_id TEXT,
    amount DECIMAL(12, 2),
    payment_method TEXT, -- cash, check, credit_card, etc.
    payment_date DATE,

    -- Full API response
    data JSONB NOT NULL,

    -- Metadata
    synced_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_payments_jobber_id ON jobber_payments(jobber_id);
CREATE INDEX IF NOT EXISTS idx_payments_invoice ON jobber_payments(invoice_jobber_id);
CREATE INDEX IF NOT EXISTS idx_payments_client ON jobber_payments(client_jobber_id);
CREATE INDEX IF NOT EXISTS idx_payments_date ON jobber_payments(payment_date);

-- =============================================================================
-- NOTES - Notes and attachments
-- =============================================================================
CREATE TABLE IF NOT EXISTS jobber_notes (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    jobber_id TEXT NOT NULL UNIQUE,

    -- Extracted fields for querying
    parent_type TEXT, -- client, job, quote, invoice
    parent_jobber_id TEXT,
    content TEXT,
    author_jobber_id TEXT,
    created_at_jobber TIMESTAMPTZ,

    -- Full API response
    data JSONB NOT NULL,

    -- Vector embedding for AI search
    embedding vector(1536),

    -- Metadata
    synced_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_notes_jobber_id ON jobber_notes(jobber_id);
CREATE INDEX IF NOT EXISTS idx_notes_parent ON jobber_notes(parent_type, parent_jobber_id);
CREATE INDEX IF NOT EXISTS idx_notes_author ON jobber_notes(author_jobber_id);

-- =============================================================================
-- SERVICES - Service types offered
-- =============================================================================
CREATE TABLE IF NOT EXISTS jobber_services (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    jobber_id TEXT NOT NULL UNIQUE,

    -- Extracted fields for querying
    name TEXT,
    description TEXT,
    default_unit_price DECIMAL(12, 2),
    is_active BOOLEAN DEFAULT true,

    -- Full API response
    data JSONB NOT NULL,

    -- Metadata
    synced_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_services_jobber_id ON jobber_services(jobber_id);
CREATE INDEX IF NOT EXISTS idx_services_name ON jobber_services(name);

-- =============================================================================
-- VECTOR INDEXES - For AI semantic search (create after data is loaded)
-- =============================================================================
-- Note: IVFFlat indexes work best with >1000 rows
-- Run these AFTER syncing data:
--
-- CREATE INDEX IF NOT EXISTS idx_clients_embedding
--     ON jobber_clients USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);
--
-- CREATE INDEX IF NOT EXISTS idx_jobs_embedding
--     ON jobber_jobs USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);
--
-- CREATE INDEX IF NOT EXISTS idx_notes_embedding
--     ON jobber_notes USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);

-- =============================================================================
-- HELPER FUNCTIONS
-- =============================================================================

-- Function to update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Apply trigger to all tables
DO $$
DECLARE
    t TEXT;
BEGIN
    FOR t IN
        SELECT table_name FROM information_schema.tables
        WHERE table_schema = 'public'
        AND table_name LIKE 'jobber_%'
        AND table_name != 'jobber_sync_log'
    LOOP
        EXECUTE format('
            DROP TRIGGER IF EXISTS update_%s_updated_at ON %s;
            CREATE TRIGGER update_%s_updated_at
            BEFORE UPDATE ON %s
            FOR EACH ROW
            EXECUTE FUNCTION update_updated_at_column();
        ', t, t, t, t);
    END LOOP;
END;
$$;

-- =============================================================================
-- VIEWS - Useful aggregations
-- =============================================================================

-- Client summary with job/invoice stats
CREATE OR REPLACE VIEW jobber_client_summary AS
SELECT
    c.id,
    c.jobber_id,
    c.name,
    c.email,
    c.company_name,
    COUNT(DISTINCT j.id) as total_jobs,
    COUNT(DISTINCT CASE WHEN j.status = 'completed' THEN j.id END) as completed_jobs,
    COUNT(DISTINCT i.id) as total_invoices,
    COALESCE(SUM(i.total), 0) as total_invoiced,
    COALESCE(SUM(i.amount_due), 0) as total_outstanding,
    MAX(j.completed_at) as last_job_completed,
    c.synced_at
FROM jobber_clients c
LEFT JOIN jobber_jobs j ON j.client_jobber_id = c.jobber_id
LEFT JOIN jobber_invoices i ON i.client_jobber_id = c.jobber_id
GROUP BY c.id, c.jobber_id, c.name, c.email, c.company_name, c.synced_at;

-- Sync status overview
CREATE OR REPLACE VIEW jobber_sync_status AS
SELECT
    entity_type,
    MAX(sync_completed_at) as last_sync,
    SUM(CASE WHEN status = 'completed' THEN records_synced ELSE 0 END) as total_records,
    COUNT(CASE WHEN status = 'failed' THEN 1 END) as failed_syncs
FROM jobber_sync_log
GROUP BY entity_type;

-- =============================================================================
-- COMMENTS
-- =============================================================================
COMMENT ON TABLE jobber_clients IS 'Customer/client records from Jobber';
COMMENT ON TABLE jobber_properties IS 'Service locations for clients';
COMMENT ON TABLE jobber_jobs IS 'Work orders/jobs';
COMMENT ON TABLE jobber_visits IS 'Scheduled appointments within jobs';
COMMENT ON TABLE jobber_quotes IS 'Estimates/quotes';
COMMENT ON TABLE jobber_invoices IS 'Billing records';
COMMENT ON TABLE jobber_line_items IS 'Line items on quotes, invoices, and jobs';
COMMENT ON TABLE jobber_payments IS 'Payment records';
COMMENT ON TABLE jobber_notes IS 'Notes and attachments on various entities';
COMMENT ON TABLE jobber_users IS 'Team members';
COMMENT ON TABLE jobber_services IS 'Service types offered';
COMMENT ON TABLE jobber_sync_log IS 'Tracks sync operations for debugging and incremental sync';

-- Done!
SELECT 'Jobber schema created successfully!' as message;

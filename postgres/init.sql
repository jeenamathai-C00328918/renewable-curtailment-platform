CREATE TABLE IF NOT EXISTS renewable_energy (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP,
    wind_generation INTEGER,
    electricity_demand INTEGER
);

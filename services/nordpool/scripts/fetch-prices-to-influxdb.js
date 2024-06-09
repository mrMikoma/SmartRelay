const nordpool = require("nordpool");
const { InfluxDB, Point } = require("@influxdata/influxdb-client");

// Load environment variables from .env file
require("dotenv").config();

// Define required environment variables
const requiredEnvVars = [
  "AREA",
  "CURRENCY",
  "HOSTNAME",
  "INFLUX_URL",
  "INFLUX_ORG",
  "INFLUX_BUCKET",
  "INFLUX_TOKEN",
];

// Check if all required environment variables are set
for (const envVar of requiredEnvVars) {
  if (!process.env[envVar]) {
    throw new Error(`${requiredEnvVars.join(", ")} must be specified`);
  }
}

// InfluxDB Connection Setup
const client = new InfluxDB({
  url: process.env.INFLUX_URL,
  token: process.env.INFLUX_TOKEN,
});

// Write API for Writes
let writeClient = client.getWriteApi(
  process.env.INFLUX_ORG,
  process.env.INFLUX_BUCKET,
  "s"
);
writeClient.useDefaultTags({ host: process.env.HOSTNAME || "unknown" });

// Fetch Nordpool prices and write them to InfluxDB
(async () => {
  const timestamp = new Date().toISOString(); // Get timestamp at the start

  try {
    console.log(
      timestamp,
      "Fetching hourly prices for",
      process.env.AREA,
      "in",
      process.env.CURRENCY
    );

    // Fetch the hourly prices for AREA and CURRENCY
    const prices = new nordpool.Prices();
    const pricesJSON = await prices.hourly({
      area: process.env.AREA,
      currency: process.env.CURRENCY,
      from: new Date(),
    });

    // Convert the prices to InfluxDB points
    const points = pricesJSON.map((priceData) => {
      const point = new Point("nordpool")
        .tag("area", priceData.area)
        .floatField("price", priceData.value)
        .timestamp(new Date(priceData.date));

      return point;
    });

    // Write the points to InfluxDB in batches
    writeClient.writePoints(points);

    await writeClient.flush();
    console.log(timestamp, "Data written to InfluxDB successfully");
  } catch (error) {
    console.error(timestamp, "Error fetching/writing Nordpool prices:", error);
  } finally {
    // Ensure the writeApi is closed
    writeClient.close();
  }
})();

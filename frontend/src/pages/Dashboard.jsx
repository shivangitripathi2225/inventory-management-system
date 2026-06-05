import { useEffect, useState } from "react";
import api from "../services/api";

function Dashboard() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetchDashboard();
  }, []);

  const fetchDashboard = async () => {
    try {
      const response = await api.get("/dashboard");

      setData(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  if (!data) {
    return <h2>Loading...</h2>;
  }

  return (
    <div style={{ padding: "20px" }}>
      <h1>Dashboard</h1>

      <h3>Total Products: {data.total_products}</h3>

      <h3>Total Customers: {data.total_customers}</h3>

      <h3>Total Orders: {data.total_orders}</h3>

      <h3>
        Low Stock Products: {data.low_stock_products}
      </h3>
    </div>
  );
}

export default Dashboard;
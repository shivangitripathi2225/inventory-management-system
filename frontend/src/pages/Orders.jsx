import { useEffect, useState } from "react";
import api from "../services/api";

function Orders() {
  const [customers, setCustomers] = useState([]);
  const [products, setProducts] = useState([]);
  const [orders, setOrders] = useState([]);

  const [formData, setFormData] = useState({
    customer_id: "",
    product_id: "",
    quantity: 1
  });

  useEffect(() => {
    fetchCustomers();
    fetchProducts();
    fetchOrders();
  }, []);

  const fetchCustomers = async () => {
    try {
      const response = await api.get("/customers");
      setCustomers(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  const fetchProducts = async () => {
    try {
      const response = await api.get("/products");
      setProducts(response.data.items);
    } catch (error) {
      console.error(error);
    }
  };

  const fetchOrders = async () => {
    try {
      const response = await api.get("/orders");
      setOrders(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  const createOrder = async (e) => {
    e.preventDefault();

    try {
      await api.post("/orders", {
        customer_id: Number(formData.customer_id),
        items: [
          {
            product_id: Number(formData.product_id),
            quantity: Number(formData.quantity)
          }
        ]
      });

      setFormData({
        customer_id: "",
        product_id: "",
        quantity: 1
      });

      fetchOrders();
      fetchProducts();
    } catch (error) {
      console.error(error);

      if (
        error.response?.data?.detail
      ) {
        alert(error.response.data.detail);
      } else {
        alert("Unable to create order");
      }
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Orders</h1>

      <form onSubmit={createOrder}>
        <div>
          <label>Customer</label>
          <br />

          <select
            value={formData.customer_id}
            onChange={(e) =>
              setFormData({
                ...formData,
                customer_id: e.target.value
              })
            }
            required
          >
            <option value="">
              Select Customer
            </option>

            {customers.map((customer) => (
              <option
                key={customer.id}
                value={customer.id}
              >
                {customer.full_name}
              </option>
            ))}
          </select>
        </div>

        <br />

        <div>
          <label>Product</label>
          <br />

          <select
            value={formData.product_id}
            onChange={(e) =>
              setFormData({
                ...formData,
                product_id: e.target.value
              })
            }
            required
          >
            <option value="">
              Select Product
            </option>

            {products.map((product) => (
              <option
                key={product.id}
                value={product.id}
              >
                {product.name}
                {" - "}
                Stock:
                {" "}
                {product.quantity}
              </option>
            ))}
          </select>
        </div>

        <br />

        <div>
          <label>Quantity</label>
          <br />

          <input
            type="number"
            min="1"
            value={formData.quantity}
            onChange={(e) =>
              setFormData({
                ...formData,
                quantity: e.target.value
              })
            }
          />
        </div>

        <br />

        <button type="submit">
          Create Order
        </button>
      </form>

      <hr />

      <h2>Orders List</h2>

      <table
        border="1"
        cellPadding="10"
        cellSpacing="0"
      >
        <thead>
          <tr>
            <th>Order ID</th>
            <th>Customer ID</th>
            <th>Total Amount</th>
            <th>Items</th>
          </tr>
        </thead>

        <tbody>
          {orders.map((order) => (
            <tr key={order.id}>
              <td>{order.id}</td>

              <td>{order.customer_id}</td>

              <td>{order.total_amount}</td>

              <td>
                {order.items.map(
                  (item, index) => (
                    <div key={index}>
                      Product:
                      {" "}
                      {item.product_id}
                      {" | "}
                      Qty:
                      {" "}
                      {item.quantity}
                    </div>
                  )
                )}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Orders;
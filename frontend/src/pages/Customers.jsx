import { useEffect, useState } from "react";
import api from "../services/api";

function Customers() {
  const [customers, setCustomers] = useState([]);

  const [formData, setFormData] = useState({
    full_name: "",
    email: "",
    phone_number: ""
  });

  useEffect(() => {
    fetchCustomers();
  }, []);

  const fetchCustomers = async () => {
    try {
      const response = await api.get("/customers");

      setCustomers(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const createCustomer = async (e) => {
    e.preventDefault();

    try {
      await api.post("/customers", formData);

      setFormData({
        full_name: "",
        email: "",
        phone_number: ""
      });

      fetchCustomers();
    } catch (error) {
      console.error(error);
      alert("Unable to create customer");
    }
  };

  const deleteCustomer = async (id) => {
    const confirmed = window.confirm(
      "Delete this customer?"
    );

    if (!confirmed) return;

    try {
      await api.delete(`/customers/${id}`);

      fetchCustomers();
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Customers</h1>

      <form onSubmit={createCustomer}>
        <div>
          <input
            type="text"
            name="full_name"
            placeholder="Full Name"
            value={formData.full_name}
            onChange={handleChange}
            required
          />
        </div>

        <br />

        <div>
          <input
            type="email"
            name="email"
            placeholder="Email"
            value={formData.email}
            onChange={handleChange}
            required
          />
        </div>

        <br />

        <div>
          <input
            type="text"
            name="phone_number"
            placeholder="Phone Number"
            value={formData.phone_number}
            onChange={handleChange}
            required
          />
        </div>

        <br />

        <button type="submit">
          Create Customer
        </button>
      </form>

      <hr />

      <h2>Customers List</h2>

      <table
        border="1"
        cellPadding="10"
        cellSpacing="0"
      >
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Phone</th>
            <th>Action</th>
          </tr>
        </thead>

        <tbody>
          {customers.map((customer) => (
            <tr key={customer.id}>
              <td>{customer.id}</td>
              <td>{customer.full_name}</td>
              <td>{customer.email}</td>
              <td>{customer.phone_number}</td>

              <td>
                <button
                  onClick={() =>
                    deleteCustomer(customer.id)
                  }
                >
                  Delete
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Customers;
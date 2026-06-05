import { useEffect, useState } from "react";
import api from "../services/api";

function Products() {
  const [products, setProducts] = useState([]);

  const [formData, setFormData] = useState({
    name: "",
    sku: "",
    price: "",
    quantity: ""
  });

  const [editingProductId, setEditingProductId] =
    useState(null);

  useEffect(() => {
    fetchProducts();
  }, []);

  const fetchProducts = async () => {
    try {
      const response = await api.get("/products");

      setProducts(response.data.items);
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

  const resetForm = () => {
    setFormData({
      name: "",
      sku: "",
      price: "",
      quantity: ""
    });

    setEditingProductId(null);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const payload = {
        name: formData.name,
        sku: formData.sku,
        price: Number(formData.price),
        quantity: Number(formData.quantity)
      };

      if (editingProductId) {
        await api.put(
          `/products/${editingProductId}`,
          payload
        );
      } else {
        await api.post(
          "/products",
          payload
        );
      }

      resetForm();

      fetchProducts();
    } catch (error) {
      console.error(error);
      alert("Operation failed");
    }
  };

  const handleEdit = (product) => {
    setEditingProductId(product.id);

    setFormData({
      name: product.name,
      sku: product.sku,
      price: product.price,
      quantity: product.quantity
    });
  };

  const handleDelete = async (id) => {
    const confirmed = window.confirm(
      "Delete this product?"
    );

    if (!confirmed) return;

    try {
      await api.delete(`/products/${id}`);

      fetchProducts();
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Products</h1>

      <form onSubmit={handleSubmit}>
        <div>
          <input
            type="text"
            name="name"
            placeholder="Product Name"
            value={formData.name}
            onChange={handleChange}
            required
          />
        </div>

        <br />

        <div>
          <input
            type="text"
            name="sku"
            placeholder="SKU"
            value={formData.sku}
            onChange={handleChange}
            required
          />
        </div>

        <br />

        <div>
          <input
            type="number"
            name="price"
            placeholder="Price"
            value={formData.price}
            onChange={handleChange}
            required
          />
        </div>

        <br />

        <div>
          <input
            type="number"
            name="quantity"
            placeholder="Quantity"
            value={formData.quantity}
            onChange={handleChange}
            required
          />
        </div>

        <br />

        <button type="submit">
          {editingProductId
            ? "Update Product"
            : "Create Product"}
        </button>

        {editingProductId && (
          <>
            {" "}
            <button
              type="button"
              onClick={resetForm}
            >
              Cancel
            </button>
          </>
        )}
      </form>

      <hr />

      <h2>Products List</h2>

      <table
        border="1"
        cellPadding="10"
        cellSpacing="0"
      >
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>SKU</th>
            <th>Price</th>
            <th>Quantity</th>
            <th>Actions</th>
          </tr>
        </thead>

        <tbody>
          {products.map((product) => (
            <tr key={product.id}>
              <td>{product.id}</td>
              <td>{product.name}</td>
              <td>{product.sku}</td>
              <td>{product.price}</td>
              <td>{product.quantity}</td>

              <td>
                <button
                  onClick={() =>
                    handleEdit(product)
                  }
                >
                  Edit
                </button>

                {" "}

                <button
                  onClick={() =>
                    handleDelete(product.id)
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

export default Products;
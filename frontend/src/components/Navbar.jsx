import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav style={{ padding: "20px", background: "#f4f4f4" }}>
      <Link to="/">Dashboard</Link>{" | "}
      <Link to="/products">Products</Link>{" | "}
      <Link to="/customers">Customers</Link>{" | "}
      <Link to="/orders">Orders</Link>
    </nav>
  );
}

export default Navbar;
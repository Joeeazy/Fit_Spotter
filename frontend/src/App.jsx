import { BrowserRouter, Route, Routes } from "react-router-dom";
import Register from "./pages/Register";
import LandingPage from "./pages/LandingPage";
import "./App.css";
import LoginPage from "./pages/LoginPage";
//import Home from "./pages/Home";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/register" element={<Register />} />
        {/* <Route element={<PrivateRoute />}>
          <Route path="/home" element={<Home />}
        </Route> */}
      </Routes>
    </BrowserRouter>
  );
}

export default App;

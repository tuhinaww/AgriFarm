import React from "react";
import Annoucne from "../components/Annoucne";
import Footer from "../components/Footer";
import Navbar from "../components/Navbar";
import NewsLetter from "../components/NewsLetter";
import Counter from "../components/Counter";

const ProductPage = () => {
  return (
    <div>
      <Annoucne />
      <Navbar />
      <div className="flex justify-center mobile:flex-col mobile:mt-4 mobile:p-3">
        <div className="flex-1 flex items-center justify-center">
          <img
            src="https://cdn.shopify.com/s/files/1/0240/7285/products/KNITPULLOVER-PISTACHIO-2_360x.jpg?v=1642545216"
            className="product_img"
            alt="product_image"
          />
        </div>
        <div className="flex-[1.3] flex flex-col items-start  justify-items-center mt-10 mobile:items-center">
          <h1 className="title text-[40px] mobile:text-[30px]">
            Potatoes
          </h1>
          <p className="disription pr-[4rem] text-justify mt-4 mobile:pr-0">
            Farm fresh potatoes delieverd fresh from farm to your home by our farmer Mr. Mithun.
          </p>
          <div className="flex flex-col place-self-start">
            <p className="mt-7 text-3xl">
              Price: <b></b>
            </p>

            <div className="colors flex mt-7 text-2xl">
              Colors
              <div className="colorSelect bg-red-600 "></div>
              <div className="colorSelect bg-blue-600 "></div>
              <div className="colorSelect bg-yellow-400 "></div>
            </div>

            <div className="mt-7 text-2xl">
              Quantity
              <select className="border-[2px] border-silver rounded-md ml-5">
                <option selected>Select</option>
                <option>500g</option>
                <option>1kg</option>
                <option>4kg</option>
                <option>8kg</option>
              </select>
            </div>
            <div className="mt-7">
              <Counter />
            </div>
          </div>

          <button className="text-white bg-[#8a4af3] rounded-md shadow-md mt-[30px] p-3">
            Add to Cart
          </button>
        </div>
      </div>
      <NewsLetter />
      <Footer />
    </div>
  );
};

export default ProductPage;
<script lang="ts">
  import svelteLogo from "./assets/svelte.svg";
  import Counter from "./lib/Counter.svelte";
  import redmoon from "./assets/redmoon.png";
  import earth from "./assets/earth.png";
  import blackhole from "./assets/blackhole.png";
  import Business from "./Business.svelte";

  import { Router, Route, Link } from "svelte-navigator";

  import routes from "./Main.svelte";
</script>

  <head>
    <title>TasteTrade</title>
    <link
      href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.15/dist/tailwind.min.css"
      rel="stylesheet"
    />
  </head>
  <body class="overflow-y-scroll min-h-screen mb-20">
    <!-- Header -->
    <header class="bg-white bg-cover bg-center">
      <div class="container mx-auto px-4">
        <div class="flex justify-between items-center py-4">
          <a href="#" class="text-lg font-bold">CookBook</a>

          <div class="flex items-center">
            <a href="#" class="text-gray-500 hover:text-gray-900 mx-4"
              >Sign Up</a
            >
            <a href="#" class="text-gray-500 hover:text-gray-900 mx-4"
              >Sign In</a
            >
          </div>
        </div>
      </div>
    </header>
    <!-- Hero Section -->
    <section
      class="bg-white bg-cover bg-center py-20 relative"
      style="background-image: url('https://img.freepik.com/free-photo/tasty-thanksgiving-food-assortment_23-2148663997.jpg?w=2000&t=st=1679752868~exp=1679753468~hmac=14f0fc54436212cf0df9c64da3ebeaa97ac91b696fc128683d8f696da0778cdb');"
    >
      <div
        class="absolute inset-0 bg-gray-900 bg-opacity-10 backdrop-blur-sm"
      />
      <div
        class="container w-1/3 text-center mx-auto border-gray-200 rounded-lg px-4 relative z-10"
      >
        <h1 class="text-white text-4xl font-bold mb-4">Craving something?</h1>
        <p class="text-white text-lg mb-8">
          Find the best home chefs and get the freshest meals and produce
        </p>
      </div>
    </section>
    <h1 class="text-black text-center text-4xl font-bold mb-4 mt-5">
      Recommended
    </h1>
    <div class="flex bg-white overflow-x-auto space-x-20 pb-1 mx-10">

      <Link to="buisiness">
        <div class="flex-shrink-0 w-64 bg-white rounded-lg shadow-md p-4">
          <img
            src="https://via.placeholder.com/256x128"
            alt="Business Logo"
            class="w-full h-32 object-cover rounded-md mb-4"
          />
          <h3 class="text-lg font-medium mb-2">Business Name</h3>
          <p class="text-gray-700">Business Description</p>
          <button
            class="mt-4 bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-md"
            >Order Now</button
          >
        </div>
      </Link>

      <div class="flex-shrink-0 w-64 bg-white rounded-lg shadow-md p-4">
        <img
          src="https://via.placeholder.com/256x128"
          alt="Business Logo"
          class="w-full h-32 object-cover rounded-md mb-4"
        />
        <h3 class="text-lg font-medium mb-2">Business Name</h3>
        <p class="text-gray-700">Business Description</p>
        <button
          class="mt-4 bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-md"
          >Order Now</button
        >
      </div>

      <div class="flex-shrink-0 w-64 bg-white rounded-lg shadow-md p-4">
        <img
          src="https://via.placeholder.com/256x128"
          alt="Business Logo"
          class="w-full h-32 object-cover rounded-md mb-4"
        />
        <h3 class="text-lg font-medium mb-2">Business Name</h3>
        <p class="text-gray-700">Business Description</p>
        <button
          class="mt-4 bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-md"
          >Order Now</button
        >
      </div>

      <div class="flex-shrink-0 w-64 bg-white rounded-lg shadow-md p-4">
        <img
          src="https://via.placeholder.com/256x128"
          alt="Business Logo"
          class="w-full h-32 object-cover rounded-md mb-4"
        />
        <h3 class="text-lg font-medium mb-2">Business Name</h3>
        <p class="text-gray-700">Business Description</p>
        <button
          class="mt-4 bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-md"
          >Order Now</button
        >
      </div>

      <div class="flex-shrink-0 w-64 bg-white rounded-lg shadow-md p-4">
        <img
          src="https://via.placeholder.com/256x128"
          alt="Business Logo"
          class="w-full h-32 object-cover rounded-md mb-4"
        />
        <h3 class="text-lg font-medium mb-2">Business Name</h3>
        <p class="text-gray-700">Business Description</p>
        <button
          class="mt-4 bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-md"
          >Order Now</button
        >
      </div>

      <div class="flex-shrink-0 w-64 bg-white rounded-lg shadow-md p-4">
        <img
          src="https://via.placeholder.com/256x128"
          alt="Business Logo"
          class="w-full h-32 object-cover rounded-md mb-4"
        />
        <h3 class="text-lg font-medium mb-2">Business Name</h3>
        <p class="text-gray-700">Business Description</p>
        <button
          class="mt-4 bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-md"
          >Order Now</button
        >
      </div>

      <div class="flex-shrink-0 w-64 bg-white rounded-lg shadow-md p-4">
        <img
          src="https://via.placeholder.com/256x128"
          alt="Business Logo"
          class="w-full h-32 object-cover rounded-md mb-4"
        />
        <h3 class="text-lg font-medium mb-2">Business Name</h3>
        <p class="text-gray-700">Business Description</p>
        <button
          class="mt-4 bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-md"
          >Order Now</button
        >
      </div>

      <!-- Add more businesses here... -->
    </div>

    <h1 class="text-black text-center text-4xl font-bold mb-4 mt-5">Produce</h1>

    <div class="flex bg-white overflow-x-auto space-x-20 pb-1 mx-10 ">
      <div class="flex-shrink-0 w-64 bg-white rounded-lg shadow-md p-4">
        <img
          src="https://via.placeholder.com/256x128"
          alt="Business Logo"
          class="w-full h-32 object-cover rounded-md mb-4"
        />
        <h3 class="text-lg font-medium mb-2">Business Name</h3>
        <p class="text-gray-700">Business Description</p>
        <button
          class="mt-4 bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-md"
          >Order Now</button
        >
      </div>

      <div class="flex-shrink-0 w-64 bg-white rounded-lg shadow-md p-4">
        <img
          src="https://via.placeholder.com/256x128"
          alt="Business Logo"
          class="w-full h-32 object-cover rounded-md mb-4"
        />
        <h3 class="text-lg font-medium mb-2">Business Name</h3>
        <p class="text-gray-700">Business Description</p>
        <button
          class="mt-4 bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-md"
          >Order Now</button
        >
      </div>

      <div class="flex-shrink-0 w-64 bg-white rounded-lg shadow-md p-4">
        <img
          src="https://via.placeholder.com/256x128"
          alt="Business Logo"
          class="w-full h-32 object-cover rounded-md mb-4"
        />
        <h3 class="text-lg font-medium mb-2">Business Name</h3>
        <p class="text-gray-700">Business Description</p>
        <button
          class="mt-4 bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-md"
          >Order Now</button
        >
      </div>

      <div class="flex-shrink-0 w-64 bg-white rounded-lg shadow-md p-4">
        <img
          src="https://via.placeholder.com/256x128"
          alt="Business Logo"
          class="w-full h-32 object-cover rounded-md mb-4"
        />
        <h3 class="text-lg font-medium mb-2">Business Name</h3>
        <p class="text-gray-700">Business Description</p>
        <button
          class="mt-4 bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-md"
          >Order Now</button
        >
      </div>

      <div class="flex-shrink-0 w-64 bg-white rounded-lg shadow-md p-4">
        <img
          src="https://via.placeholder.com/256x128"
          alt="Business Logo"
          class="w-full h-32 object-cover rounded-md mb-4"
        />
        <h3 class="text-lg font-medium mb-2">Business Name</h3>
        <p class="text-gray-700">Business Description</p>
        <button
          class="mt-4 bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-md"
          >Order Now</button
        >
      </div>

      <div class="flex-shrink-0 w-64 bg-white rounded-lg shadow-md p-4">
        <img
          src="https://via.placeholder.com/256x128"
          alt="Business Logo"
          class="w-full h-32 object-cover rounded-md mb-4"
        />
        <h3 class="text-lg font-medium mb-2">Business Name</h3>
        <p class="text-gray-700">Business Description</p>
        <button
          class="mt-4 bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-md"
          >Order Now</button
        >
      </div>

      <div class="flex-shrink-0 w-64 bg-white rounded-lg shadow-md p-4">
        <img
          src="https://via.placeholder.com/256x128"
          alt="Business Logo"
          class="w-full h-32 object-cover rounded-md mb-4"
        />
        <h3 class="text-lg font-medium mb-2">Business Name</h3>
        <p class="text-gray-700">Business Description</p>
        <button
          class="mt-4 bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-md"
          >Order Now</button
        >
      </div>

      <!-- Add more businesses here... -->
    </div>

    <h1 class="text-black text-center text-4xl font-bold mb-4 mt-5">
      Home Cooks
    </h1>

    <div class="flex bg-white overflow-x-auto space-x-20 pb-20 mx-10 ">
      <div class="flex-shrink-0 w-64 bg-white rounded-lg shadow-md p-4">
        <img
          src="https://via.placeholder.com/256x128"
          alt="Business Logo"
          class="w-full h-32 object-cover rounded-md mb-4"
        />
        <h3 class="text-lg font-medium mb-2">Business Name</h3>
        <p class="text-gray-700">Business Description</p>
        <button
          class="mt-4 bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-md"
          >Order Now</button
        >
      </div>

      <div class="flex-shrink-0 w-64 bg-white rounded-lg shadow-md p-4">
        <img
          src="https://via.placeholder.com/256x128"
          alt="Business Logo"
          class="w-full h-32 object-cover rounded-md mb-4"
        />
        <h3 class="text-lg font-medium mb-2">Business Name</h3>
        <p class="text-gray-700">Business Description</p>
        <button
          class="mt-4 bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-md"
          >Order Now</button
        >
      </div>

      <div class="flex-shrink-0 w-64 bg-white rounded-lg shadow-md p-4">
        <img
          src="https://via.placeholder.com/256x128"
          alt="Business Logo"
          class="w-full h-32 object-cover rounded-md mb-4"
        />
        <h3 class="text-lg font-medium mb-2">Business Name</h3>
        <p class="text-gray-700">Business Description</p>
        <button
          class="mt-4 bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-md"
          >Order Now</button
        >
      </div>

      <div class="flex-shrink-0 w-64 bg-white rounded-lg shadow-md p-4">
        <img
          src="https://via.placeholder.com/256x128"
          alt="Business Logo"
          class="w-full h-32 object-cover rounded-md mb-4"
        />
        <h3 class="text-lg font-medium mb-2">Business Name</h3>
        <p class="text-gray-700">Business Description</p>
        <button
          class="mt-4 bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-md"
          >Order Now</button
        >
      </div>

      <div class="flex-shrink-0 w-64 bg-white rounded-lg shadow-md p-4">
        <img
          src="https://via.placeholder.com/256x128"
          alt="Business Logo"
          class="w-full h-32 object-cover rounded-md mb-4"
        />
        <h3 class="text-lg font-medium mb-2">Business Name</h3>
        <p class="text-gray-700">Business Description</p>
        <button
          class="mt-4 bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-md"
          >Order Now</button
        >
      </div>

      <div class="flex-shrink-0 w-64 bg-white rounded-lg shadow-md p-4">
        <img
          src="https://via.placeholder.com/256x128"
          alt="Business Logo"
          class="w-full h-32 object-cover rounded-md mb-4"
        />
        <h3 class="text-lg font-medium mb-2">Business Name</h3>
        <p class="text-gray-700">Business Description</p>
        <button
          class="mt-4 bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-md"
          >Order Now</button
        >
      </div>

      <div class="flex-shrink-0 w-64 bg-white rounded-lg shadow-md p-4">
        <img
          src="https://via.placeholder.com/256x128"
          alt="Business Logo"
          class="w-full h-32 object-cover rounded-md mb-4"
        />
        <h3 class="text-lg font-medium mb-2">Business Name</h3>
        <p class="text-gray-700">Business Description</p>
        <button
          class="mt-4 bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded-md"
          >Order Now</button
        >
      </div>

      <!-- Add more businesses here... -->
    </div>

    <!-- Footer -->
    <footer class="bg-gray-800 text-white py-8 w-full">
      <div class="container mx-auto px-4">
        <nav class="flex justify-between items-center">
          <a href="#" class="text-lg font-bold">CookBook</a>
          <div class="flex">
            <a href="#" class="text-gray-500 hover:text-white mx-4">About Us</a>
            <a href="#" class="text-gray-500 hover:text-white mx-4"
              >Contact Us</a
            >
            <a href="#" class="text-gray-500 hover:text-white mx-4"
              >Privacy Policy</a
            >
          </div>
        </nav>
      </div>
    </footer>
  </body>




<style>
  /* html, body {
  height: 100%;
  margin: 0;
} */
  footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    color: white;
    text-align: center;
  }
  .logo {
    height: 6em;
    padding: 1.5em;
    will-change: filter;
  }
  .logo:hover {
    filter: drop-shadow(0 0 2em #646cffaa);
  }
  .logo.svelte:hover {
    filter: drop-shadow(0 0 2em #ff3e00aa);
  }
  .read-the-docs {
    color: rgba(136, 136, 136, 0);
  }
</style>

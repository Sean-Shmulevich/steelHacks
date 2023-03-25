<script lang="ts">
  import svelteLogo from "./assets/svelte.svg";
  import Counter from "./lib/Counter.svelte";
  import redmoon from "./assets/redmoon.png";
  import earth from "./assets/earth.png";
  import blackhole from "./assets/blackhole.png";
  import { Link } from "svelte-router";
</script>

<head>
  <title>TasteTrade</title>
  <link
    href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.15/dist/tailwind.min.css"
    rel="stylesheet"
  />
</head>
<body class="overflow-y-scroll min-h-screen mb-20">
  <h1>Hello</h1>
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

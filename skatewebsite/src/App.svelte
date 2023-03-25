<script>
  import { Router, Route } from 'svelte-routing';
  import HomePage from './Main.svelte';
  import Buisiness from './Business.svelte';
  import { Link } from 'svelte-routing';
</script>


<Router>
  <Route path="/" component={HomePage} />
  <Route path="/about" component={Buisiness} />
</Router>
<nav>
  <ul>
    <li><Link to="/">Home</Link></li>
    <li><Link to="/about">About</Link></li>
  </ul>
</nav>

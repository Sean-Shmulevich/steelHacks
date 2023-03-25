<script>
	let menuItems = [];
	let menuFoods = [];
	let reviews = [];

	const fetchData = async () => {
		const response = await fetch('http://0.0.0.0:8000/bus/0');
		const data = await response.json();
		menuItems = data;
	};

	const fetchDataMenu = async () => {
		const response = await fetch('http://0.0.0.0:8000/food');
		const data = await response.json();
		menuFoods = data;
	};

	const fetchDataReviews = async () => {
		const response = await fetch('http://0.0.0.0:8000/reviews');
		const data = await response.json();
		reviews = data;
	};

	fetchData();
	fetchDataMenu();
	fetchDataReviews();
</script>

<head>
	<title>CookBook</title>
	<link
		href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.15/dist/tailwind.min.css"
		rel="stylesheet"
	/>
</head>
<main class="container mx-auto px-4">
	<header class="bg-white bg-cover bg-center">
		<div class="container mx-auto px-4">
			<div class="flex justify-between items-center py-4">
				<a href="/" class="text-lg font-bold">CookBook</a>

				<div class="flex items-center">
					<a href="#" class="text-gray-500 hover:text-gray-900 mx-4">Sign Up</a>
					<a href="#" class="text-gray-500 hover:text-gray-900 mx-4">Sign In</a>
				</div>
			</div>
		</div>
	</header>
	<div class="flex flex-col lg:flex-row h-screen w-full">
		<div
			class="w-full lg:w-2/3 bg-gray-100"
			style="position:absolute;right:0px;width:40%;top:100px"
		>
			<div class="max-w-screen-lg mx-auto px-6 py-16">
				<h1 class="text-3xl font-bold mb-8">Menu</h1>
				<ul>
					{#each menuFoods as food, i}
						{#if i < 5}
							<li class="mb-8">
								<div class="flex items-center justify-between">
									<h2 class="text-lg font-medium">{food.name}</h2>
									<p class="text-lg font-medium">${food.price}</p>
								</div>
								<p class="text-gray-500 mt-2">{food.description}</p>
							</li>
						{/if}
					{/each}
				</ul>
			</div>
		</div>
		<div class="flex" style="position:absolute;left:-30%;top:100px">
			<div class="mx-auto bg-white rounded-lg shadow-lg overflow-hidden" style="width:40%">
				<div class="relative">
					<img
						src="https://img.freepik.com/free-photo/tasty-thanksgiving-food-assortment_23-2148663997.jpg?w=2000&t=st=1679752868~exp=1679753468~hmac=14f0fc54436212cf0df9c64da3ebeaa97ac91b696fc128683d8f696da0778cdb"
						alt="Business"
					/>
					<div
						class="absolute bottom-0 left-0 w-full h-16 bg-white opacity-75 flex items-center justify-center"
					>
						<span class="text-4xl text-gray-700 mr-2 font-bold" style="margin-top:-10px"
							>{menuItems.avg_stars}</span
						>
						<svg
							xmlns="http://www.w3.org/2000/svg"
							class="h-8 w-8 text-yellow-500"
							style="width:30px;"
							viewBox="0 0 20 20"
							fill="currentColor"
						>
							<path
								fill-rule="evenodd"
								d="M10 14.949L4.577 19l1.045-6.061L1.55 7.435l6.098-.885L10 1l2.352 5.55 6.098.885-4.072 3.504L15.423 19z"
								clip-rule="evenodd"
							/>
						</svg>
						<svg
							xmlns="http://www.w3.org/2000/svg"
							class="h-8 w-8 text-yellow-500"
							style="width:30px;"
							viewBox="0 0 20 20"
							fill="currentColor"
						>
							<path
								fill-rule="evenodd"
								d="M10 14.949L4.577 19l1.045-6.061L1.55 7.435l6.098-.885L10 1l2.352 5.55 6.098.885-4.072 3.504L15.423 19z"
								clip-rule="evenodd"
							/>
						</svg>
						<svg
							xmlns="http://www.w3.org/2000/svg"
							class="h-8 w-8 text-yellow-500"
							style="width:30px;"
							viewBox="0 0 20 20"
							fill="currentColor"
						>
							<path
								fill-rule="evenodd"
								d="M10 14.949L4.577 19l1.045-6.061L1.55 7.435l6.098-.885L10 1l2.352 5.55 6.098.885-4.072 3.504L15.423 19z"
								clip-rule="evenodd"
							/>
						</svg>
					</div>
				</div>
				<div class="p-4">
					<h1 class="text-3xl text-center font-bold mb-2">{menuItems._name}</h1>
					<p class="text-gray-600 text-lg">{menuItems._bio}</p>
				</div>
			</div>
		</div>
		<div
			class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6"
			style="margin-top:800px;padding-bottom:500px"
		>
			<!-- First review -->
			{#each reviews as review}
				<div class="bg-white shadow-lg rounded-lg px-4 py-6">
					<p class="text-gray-700 font-medium mb-4">{review._sent}</p>
					<p class="text-gray-500 text-sm">- {review._stars} Stars</p>
				</div>
			{/each}
		</div>
	</div>
	<footer class="bg-gray-800 text-white py-8 w-full">
		<div class="container mx-auto px-4">
			<nav class="flex justify-between items-center">
				<a href="#" class="text-lg font-bold">CookBook</a>
				<div class="flex">
					<a href="#" class="text-gray-500 hover:text-white mx-4">About Us</a>
					<a href="#" class="text-gray-500 hover:text-white mx-4">Contact Us</a>
					<a href="#" class="text-gray-500 hover:text-white mx-4">Privacy Policy</a>
				</div>
			</nav>
		</div>
	</footer>
</main>

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
</style>

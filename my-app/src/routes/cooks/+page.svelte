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
					<ul>
						{#each menuItems as menuItem}
							<li class="mb-8">
								<div class="flex items-center justify-between">
									<h2 class="text-lg font-medium">{menuItem.name}</h2>
									<p class="text-lg font-medium">${menuItem.price}</p>
								</div>
								<p class="text-gray-500 mt-2">{menuItem.description}</p>
							</li>
						{/each}
					</ul>
					<li class="mb-8">
						<div class="flex items-center justify-between">
							<h2 class="text-lg font-medium">Roast Chicken</h2>
							<p class="text-lg font-medium">$15</p>
						</div>
						<p class="text-gray-500 mt-2">Description of the Roast Chicken dish goes here.</p>
					</li>
					<li class="mb-8">
						<div class="flex items-center justify-between">
							<h2 class="text-lg font-medium">Grilled Fish</h2>
							<p class="text-lg font-medium">$18</p>
						</div>
						<p class="text-gray-500 mt-2">Description of the Grilled Fish dish goes here.</p>
					</li>
					<li class="mb-8">
						<div class="flex items-center justify-between">
							<h2 class="text-lg font-medium">Vegetable Curry</h2>
							<p class="text-lg font-medium">$12</p>
						</div>
						<p class="text-gray-500 mt-2">Description of the Vegetable Curry dish goes here.</p>
					</li>
					<li class="mb-8">
						<div class="flex items-center justify-between">
							<h2 class="text-lg font-medium">Beef Stew</h2>
							<p class="text-lg font-medium">$20</p>
						</div>
						<p class="text-gray-500 mt-2">Description of the Beef Stew dish goes here.</p>
					</li>
					<li class="mb-8">
						<div class="flex items-center justify-between">
							<h2 class="text-lg font-medium">Pasta Carbonara</h2>
							<p class="text-lg font-medium">$14</p>
						</div>
						<p class="text-gray-500 mt-2">Description of the Pasta Carbonara dish goes here.</p>
					</li>
					<li class="mb-8">
						<div class="flex items-center justify-between">
							<h2 class="text-lg font-medium">Salmon Salad</h2>
							<p class="text-lg font-medium">$16</p>
						</div>
						<p class="text-gray-500 mt-2">Description of the Salmon Salad dish goes here.</p>
					</li>
				</ul>
			</div>
		</div>
		<div class="flex" style="position:absolute;left:-19%;top:100px">
			<div class="w-3/5 mx-auto bg-white rounded-lg shadow-lg overflow-hidden">
				<div class="relative">
					<img
						src="https://img.freepik.com/free-photo/tasty-thanksgiving-food-assortment_23-2148663997.jpg?w=2000&t=st=1679752868~exp=1679753468~hmac=14f0fc54436212cf0df9c64da3ebeaa97ac91b696fc128683d8f696da0778cdb"
						alt="Business"
					/>
					<div
						class="absolute bottom-0 left-0 w-full h-16 bg-white opacity-75 flex items-center justify-center"
					>
						<span class="text-4xl text-gray-700 mr-2 font-bold" style="margin-top:-10px">4.5</span>
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
					<h1 class="text-3xl text-center font-bold mb-2">Business Name</h1>
					<p class="text-gray-600 text-lg">Description of the business goes here.</p>
				</div>
			</div>
		</div>
		<div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6" style="margin-top:1000px">
			<!-- First review -->
			<div class="bg-white shadow-lg rounded-lg px-4 py-6">
				<p class="text-gray-700 font-medium mb-4">
					"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed ipsum in neque malesuada
					blandit. Nam id porta justo."
				</p>
				<p class="text-gray-500 text-sm">- John Doe, Happy Customer</p>
			</div>

			<!-- Second review -->
			<div class="bg-white shadow-lg rounded-lg px-4 py-6">
				<p class="text-gray-700 font-medium mb-4">
					"Vestibulum vel enim a augue dictum laoreet. Fusce sed turpis ullamcorper, mattis velit
					nec, ultrices quam."
				</p>
				<p class="text-gray-500 text-sm">- Jane Smith, Satisfied Customer</p>
			</div>

			<!-- Third review -->
			<div class="bg-white shadow-lg rounded-lg px-4 py-6">
				<p class="text-gray-700 font-medium mb-4">
					"Nulla facilisi. Morbi aliquet gravida libero, ut lacinia mi bibendum at. Nam euismod
					massa vel urna eleifend fringilla."
				</p>
				<p class="text-gray-500 text-sm">- James Johnson, Repeat Customer</p>
			</div>
		</div>
	</div>
</main>

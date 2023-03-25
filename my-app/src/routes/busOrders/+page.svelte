<script>
	import { onMount } from 'svelte';

	let data;

	async function fetchDataJSON() {
		const response = await fetch('http://127.0.0.1:8000/bus/orders');
		const data = await response.json();
		return data;
	}

	onMount(async () => {
		data = await fetchDataJSON();

		const table = document.querySelector('#orderData');

		// create table header
		const headerRow = table.insertRow();
		Object.keys(data[0]).forEach((key) => {
			const headerCell = document.createElement('th');
			const text = document.createTextNode(key);
			headerCell.appendChild(text);
			headerRow.appendChild(headerCell);
		});


	});
</script>

<main class="container mx-auto px-4 py-8">
	<div class="flex justify-between items-center mb-8">
		<h2 class="text-2xl font-bold text-secondary">Current Orders</h2>
		<div class="relative">
			<input
				type="text"
				placeholder="Search"
				class="rounded-full px-4 py-2 border-secondary focus:outline-none focus:ring-2 focus:ring-primary"
			/>
			<button
				class="absolute right-0 top-0 bottom-0 px-4 py-2 rounded-full bg-primary text-white hover:bg-secondary transition duration-300"
			>
				<i class="fas fa-search" />
			</button>
		</div>
	</div>

	<table class="w-full" id="orderData">
		<thead>
			<tr>
				<th class="text-left text-secondary uppercase font-bold text-sm tracking-wider py-3">
					Order ID
				</th>
				<th class="text-left text-secondary uppercase font-bold text-sm tracking-wider py-3">
					Customer Name
				</th>
				<th class="text-left text-secondary uppercase font-bold text-sm tracking-wider py-3">
					Businesss Name
				</th>
				<th class="text-left text-secondary uppercase font-bold text-sm tracking-wider py-3">
					Order Date
				</th>
				<th class="text-left text-secondary uppercase font-bold text-sm tracking-wider py-3">
					Order Total
				</th>
				<th class="text-right text-secondary uppercase font-bold text-sm tracking-wider py-3">
					Status
				</th>
			</tr>
		</thead>
		<tbody>
			{#each orders as order}
				<tr class="bg-secondary hover:bg-gray-200 transition duration-300">
					<td class="border-b border-secondary py-4">{order._oID}</td>
					<td class="border-b border-secondary py-4">{order._custName}</td>
					<td class="border-b border-secondary py-4">{order._busName}</td>
					<td class="border-b border-secondary py-4">{new Date(order._date).toLocaleString()}</td>
					<td class="border-b border-secondary py-4">{order._total}</td>
				</tr>
			{/each}
		</tbody>
	</table>
</main>

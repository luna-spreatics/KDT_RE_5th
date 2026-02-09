import ProductList from '../components/ProductList';

function ProductPage({ products }) {
	return (
		<div>
			<h1>Product Page</h1>
			<ProductList products={products} />
		</div>
	);
}

export default ProductPage;

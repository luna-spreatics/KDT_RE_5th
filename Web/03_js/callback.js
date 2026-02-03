// console.log(1);
// setTimeout(function () {
// 	console.log(2);
// }, 2000);
// console.log(3);

//////////////////////////
// ex. 편의점 -> 음료를 고르고 -> 산다
/*
function goMart() {
	console.log('마트에 가서 어떤 음료 살지 고민...');
}

function pickDrink() {
	// 3초 고민 후에 결정
	setTimeout(function () {
		console.log('고민끝!');
		product = '제로콜라';
		price = 2000;
	}, 3000);
}

function pay() {
	console.log(`상품명: ${product}, 가격: ${price}`);
}

let product;
let price;
goMart();
pickDrink();
pay();
*/

////////////////////////////////////////
// 1. 콜백 함수를 이용해 비동기 처리

function goMart() {
	console.log('마트에 가서 어떤 음료 살지 고민...');
}

function pickDrink(callback) {
	// 3초 고민 후에 결정
	setTimeout(function () {
		console.log('고민끝!');
		product = '제로콜라';
		price = 2000;
		callback(); // 매개변수로 넘긴 콜백함수를 실행
	}, 3000);
}

function pay() {
	console.log(`상품명: ${product}, 가격: ${price}`);
}

let product;
let price;
goMart();
pickDrink(pay);

/////////////////////////
function call(name, cb) {
	setTimeout(function () {
		console.log(name);
		cb(name);
	}, 1000);
}

function back(cb) {
	setTimeout(function () {
		console.log('back');
		cb('back');
	}, 1000);
}

function hell(cb) {
	setTimeout(function () {
		cb('callback hell');
	}, 1000);
}

// call -> back -> hell 순서로 실행
call('kim', function (name) {
	console.log(name + '반가워');

	back(function (txt) {
		console.log(txt + '을 실행했구나');

		hell(function (message) {
			console.log('여기는 ' + message);
		});
	});
});

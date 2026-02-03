async function f1() {
	return 1;
}

console.log(f1());

//////////////////////////////
/**
 * async - await
 * async : 함수 앞에 붙이는 키워드
 * - 함수만 보고도 비동기 함수임을 유추하고자 함
 * - 프로미스를 반환
 *
 * await: 기다리다
 * - 성공/실패로 프로미스 객체의 실행이 완료되기를 기다림
 * - await 뒤에는 프로미스가 오게 됨
 * - async 키워드를 사용한 함수 안에서만 await 키워드 사용 가능
 */

///////////////////////////////////////
// function goMart() {
// 	console.log('마트에 가서 어떤 음료 살지 고민...');
// }

// function pickDrink() {
// 	return new Promise((resolve, reject) => {
// 		// 3초 고민 후에 결정
// 		setTimeout(function () {
// 			console.log('고민끝!');
// 			product = '제로콜라';
// 			price = 2000;
// 			resolve();
// 		}, 3000);
// 	});
// }

// function pay() {
// 	console.log(`상품명: ${product}, 가격: ${price}`);
// }

// async function exec() {
// 	goMart();
// 	await pickDrink();
// 	pay();
// }

// let product;
// let price;
// exec();

////////////////////////
// 실습

function call(name) {
	return new Promise(function (resolve, reject) {
		setTimeout(function () {
			console.log(name);
			resolve(name); // 작업 성공시 then(name)
		}, 1000);
	});
}

function back() {
	return new Promise(function (resolve, reject) {
		setTimeout(function () {
			console.log('back');
			resolve('back'); // 작업 성공시 then('back')
		}, 1000);
	});
}

function hell() {
	return new Promise(function (resolve, reject) {
		setTimeout(function () {
			resolve('callback hell');
		}, 1000);
	});
}

async function exec() {
	const name = await call('kim');
	console.log(`${name} 반가워`);

	const result = await back();
	console.log(`${result}을 실행했구나`);

	const msg = await hell();
	console.log(`여기는 ${msg}`);
}

exec();

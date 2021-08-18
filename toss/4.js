class Request {
    static token = undefined;
    static pending_requests = [];

    static request() {

    }
}

async function solution(callAPI) {
    const { result, token } = await callAPI();

    // 두 번째로 `solution`이 호출될 때는 다음과 같이 이전에 반환된 `token`을 `callAPI`의 인자로 넘겨줍니다.
    // callAPI(token);

    return result;
}
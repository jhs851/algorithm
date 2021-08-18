/* 코드 주인 정보 예시 */
const codeOwnersMap = {
    "scripts": ["배수진"],
    "services": {
        "business-ledger": ["고찬균", "배수진"],
        "toss-card": ["채주민", "유재섭"],
        "payments": ["유재섭"],
    }
}

/*
 * `codeOwnersMap`과 `directory`를 입력받아
 * `directory`의 코드 주인 목록을 반환하는 함수를 작성하세요.
 */
function solution(codeOwnersMap, directory) {
    let _codeOwnersMap = { ...codeOwnersMap };

    directory.split("/").forEach(depth => {
        _codeOwnersMap = _codeOwnersMap[depth]
    });

    return _codeOwnersMap;
}

console.log(solution(codeOwnersMap, "scripts"));
console.log(solution(codeOwnersMap, "services/business-ledger"));
console.log(solution(codeOwnersMap, "services/payments"));
const solution = places => {
    return places.map(place => {
        const rowLen = place.length;

        for (let i = 0; i < rowLen; i++) {
            // 열에 응시자가 없으면 다음 열로
            if (!place[i].includes('P')) {
                continue;
            }

            const columnLen = place[i].length;

            for (let j = 0; j < columnLen; j++) {
                if (place[i][j] === 'P' && ((
                    // 응시자 상하좌우에 다른 응시자가 있으면
                    (j > 0 && place[i][j - 1] === 'P') ||
                    (j < columnLen - 1 && place[i][j + 1] === 'P') ||
                    (i > 0 && place[i - 1][j] === 'P') ||
                    (i < rowLen - 1 && place[i + 1][j] === 'P')
                ) || (
                    // 응시자 대각선상에 다른 응시자가 있고, 대각선 좌우에 파티션이 하나라도 없다면
                    ((i < rowLen - 1 && j < columnLen - 1) && place[i + 1][j + 1] === 'P' && (place[i + 1][j] === 'O' || place[i][j + 1] === 'O')) ||
                    ((i < rowLen - 1 && j > 0) && place[i + 1][j - 1] === 'P' && (place[i + 1][j] === 'O' || place[i][j - 1] === 'O')) ||
                    ((i > 0 && j > 0) && place[i - 1][j - 1] === 'P' && (place[i - 1][j] === 'O' || place[j][j - 1] === 'O')) ||
                    ((i > 0 && j < columnLen - 1) && place[i - 1][j + 1] === 'P' && (place[i - 1][j] === 'O' || place[j][j + 1] === 'O'))
                ) || (
                    // 응시자와 한칸 떨어져있는 곳에 다른 응시자가 있고, 그 사이가 테이블이라면
                    (i < rowLen - 2 && place[i + 2][j] === 'P' && place[i + 1][j] === 'O') ||
                    (j > 1 && place[i][j - 2] === 'P' && place[i][j - 1] === 'O') ||
                    (i > 1 && place[i - 2][j] === 'P' && place[i - 1][j] === 'O') ||
                    (j < columnLen - 2 && place[i][j + 2] === 'P' && place[i][j + 1] === 'O')
                ))) {
                    return 0;
                }
            }
        }

        return 1;
    });
};

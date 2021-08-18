class Element {
    type;
    id;
    listener;
    parent;
    child;

    constructor(type, id, listener) {
        this.type = type;
        this.id = id;
        this.listener = listener;
    }

    addChild(element) {
        if (element === this.parent) {
            throw new Error(`에러 발생: ${element.id}는 ${this.id}의 부모임`);
        }

        if (element.parent) {
            throw new Error(`에러 발생: ${element.id}는 이미 ${element.parent.id}을 부모로 가지고 있음`)
        }

        element.parent = this;
        this.child = element;
    }

    removeChild(element) {
        if (this.child !== element) {
            throw new Error(`에러 발생: ${element.id}은 ${this.id}의 자식이 아님`);
        }

        this.child = undefined;
    }

    onEvent(event) {
        this.listener(event);

        if (this.parent) {
            this.parent.onEvent(event);
        }
    }
}

function solution(type, id, listener) {
    return new Element(type, id, listener);
}

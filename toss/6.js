class CheckItem {
    static from(...args) {
        return new CheckItem(...args);
    }

    id;
    state = "unchecked";
    children = [];

    constructor({ id, children }) {
        this.id = id;
        this.children = children.map(child => ({ ...child, state: "unchecked" }));
    }

    toggle() {
        this.state !== "checked" ? this.check() : this.uncheck();
    }

    check() {
        this.state = "check";
        let children = this
        this.children.forEach(child => {
            while (child) {

            }
        });
    }

    uncheck() {
        this.state = "unchecked";
        this.children.forEach(child => child.uncheck());
    }
}


/**
 * ---------------------------------------------------------
 * 채점을 위한 코드입니다.
 * 수정하면 정상적인 채점이 되지 않습니다.
 * 수정하지 말아주세요.
 * ---------------------------------------------------------
 */
function solution() {
    return { CheckItem };
}
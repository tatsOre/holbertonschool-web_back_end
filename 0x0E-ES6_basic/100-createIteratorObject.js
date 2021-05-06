export default function createIteratorObject(report) {
  const allEmp = Object.values(report.allEmployees).flat();
  return {
    [Symbol.iterator]() {
      let current = 0;
      let last = allEmp.length;
      return {
        next() {
          if (current < last) {
            return { done: false, value: allEmp[current++] };
          } else {
            return { done: true, value: undefined };
          }
        }
      };
    }
  };
}

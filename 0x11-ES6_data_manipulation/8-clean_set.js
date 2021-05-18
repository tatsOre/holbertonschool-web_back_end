export default function cleanSet(set, startString) {
  if (!startString) return '';

  const cleanSet = [...set].map((word) => {
    let sliced;
    if (word.startsWith(startString)) {
      sliced = word.substring(startString.length);
    }
    return sliced;
  });
  return cleanSet.join('-').slice(0, -1);
}

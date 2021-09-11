const dic = {
  수성: "Mercury",
  금성: "Venus",
  지구: "Earth",
  화성: "Mars",
  목성: "Jupiter",
  토성: "Saturn",
  천왕성: "Uranus",
  해왕성: "Neptune",
};

function korToEng(kor) {
  if (Object.keys(dic).includes(kor)) {
    return dic[kor];
  }
}

console.log(korToEng("해왕성"));

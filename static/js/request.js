let imgBoxTop = document.getElementById('imgBoxTop');
let imgBoxFull = document.getElementById('imgBoxFull');
let imgBoxOrigin = document.getElementById('imgBoxOrigin');

let btnBox = document.getElementById('btnBox');
let nameButtons = new Array();

let loadWindow = 100;
let currentName = '';
let nextIdx = 0;


function addLoadButton(){
    if(nextIdx == imgOrigin[currentName].length)
        return ;

    let loadBtn = document.createElement("BUTTON");
    loadBtn.classList.add('btn');
    loadBtn.classList.add('btn-outline-dark');
    loadBtn.classList.add('btn-load');
    loadBtn.innerText = "+";
    loadBtn.addEventListener('click', function () {
        loadMore();
    });
    imgBoxOrigin.appendChild(loadBtn);
}


function loadMore(){
    imgBoxOrigin.lastChild.remove();
    let endIdx = Math.min(imgOrigin[currentName].length, nextIdx + loadWindow);
    for(; nextIdx < endIdx; nextIdx++){
        let newImg = document.createElement("IMG");
        newImg.setAttribute('src', imgOrigin[currentName][nextIdx]);
        newImg.classList.add('img-list-sm');
        imgBoxOrigin.appendChild(newImg);
    }
    addLoadButton();
}


function resetBox(imgBox, filelist, fileclass, maxCount){
    while(imgBox.firstChild){
        imgBox.firstChild.remove();
    }

    let count = 0;
    for(let filename of filelist){
        let newImg = document.createElement("IMG");
        newImg.setAttribute('src', filename);
        newImg.classList.add(fileclass);
        imgBox.appendChild(newImg);
        if(++count == maxCount) break;
    }
    return count;
}


function clickNameButton(nameBtn, name){
    if(currentName == name)
        return ;

    currentName = name;
    resetBox(imgBoxTop, imgTop[name], 'img-list-md', 10);
    resetBox(imgBoxFull, imgFull[name], 'img-list-md', 10);
    nextIdx = resetBox(imgBoxOrigin, imgOrigin[name], 'img-list-sm', loadWindow);
    addLoadButton();
}


for(let i = 0; i < names.length; i++){
    nameButtons.push(document.createElement("BUTTON"));
    nameButtons[i].classList.add('btn');
    nameButtons[i].classList.add('btn-outline-dark');
    nameButtons[i].classList.add('btn-name');
    nameButtons[i].innerHTML = names[i];
    btnBox.appendChild(nameButtons[i]);
    nameButtons[i].addEventListener('click', function () {
        clickNameButton(this, names[i]);
    });
}

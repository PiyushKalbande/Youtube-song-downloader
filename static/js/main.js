const form = document.getElementById("downloadForm");
const bar = document.getElementById("progressBar");
const text = document.getElementById("progressText");
const formatSelect = document.getElementById("format");
const qualitySelect = document.getElementById("quality");

/* ---------- QUALITY HANDLER ---------- */

function updateQualityOptions() {
  qualitySelect.innerHTML = "";

  if (formatSelect.value === "mp3") {
    qualitySelect.innerHTML = `
      <option value="128">128 kbps</option>
      <option value="192" selected>192 kbps</option>
      <option value="320">320 kbps</option>
    `;
  } else {
    qualitySelect.innerHTML = `
      <option value="360">360p</option>
      <option value="480">480p</option>
      <option value="720" selected>720p</option>
      <option value="1080">1080p</option>
    `;
  }
}

updateQualityOptions();
formatSelect.addEventListener("change", updateQualityOptions);

/* ---------- DOWNLOAD + PROGRESS ---------- */

form.addEventListener("submit", function (e) {
  e.preventDefault(); // 🔥 VERY IMPORTANT

  bar.style.width = "0%";
  text.innerText = "Starting download...";
  text.style.color = "#fff";

  const uid = crypto.randomUUID();

  const uidInput = document.createElement("input");
  uidInput.type = "hidden";
  uidInput.name = "uid";
  uidInput.value = uid;
  form.appendChild(uidInput);

  const evtSource = new EventSource(`/progress/${uid}`);

  evtSource.onmessage = function (e) {
    if (e.data === "ERROR") {
      text.innerText = "❌ Invalid URL or download failed.";
      text.style.color = "red";
      bar.style.width = "0%";
      evtSource.close();
      return;
    }

    bar.style.width = e.data;
    text.innerText = `Downloading: ${e.data}`;

    if (e.data === "100%") {
      text.innerText = "✅ Download complete!";
      evtSource.close();
    }
  };

  form.submit(); // 🔥 submit AFTER SSE is ready
});

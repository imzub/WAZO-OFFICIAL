"use strict";

const assert = require("node:assert/strict");
const crypto = require("node:crypto");
const fs = require("node:fs");
const http = require("node:http");
const net = require("node:net");
const os = require("node:os");
const path = require("node:path");
const { spawn, spawnSync } = require("node:child_process");

const SOURCE_COMMIT = "7c63be818372307dc08ff6551b7296fca863d3e7";
const DEFAULT_FPS = 6;
const JPEG_QUALITY = 74;
const MINIMUM_FREE_BYTES = 320 * 1024 * 1024;
const ESTIMATED_CAPTURE_BYTES = [110 * 1024 * 1024, 220 * 1024 * 1024];
const viewport = {
  cssWidth: 2400,
  cssHeight: 1350,
  deviceScaleFactor: 0.8,
  outputWidth: 1920,
  outputHeight: 1080,
};

const sourceDirectory = __dirname;
const narratedDirectory = path.resolve(sourceDirectory, "..");
const sourceAppDirectory = path.resolve(
  process.env.WAZO_APP_SOURCE?.trim() || path.join(narratedDirectory, "source-app-v1.1.4"),
);
const historicalHarnessPath = path.join(sourceAppDirectory, "scripts", "capture-store-screenshots.js");
const timelinePath = path.join(sourceDirectory, "timeline.json");
const framesDirectory = path.join(narratedDirectory, "capture-frames");
const manifestPath = path.join(narratedDirectory, "manifests", "capture-manifest.json");
const electronPath = resolveElectronPath();

function findExecutableOnPath(name) {
  const directories = (process.env.PATH || "").split(path.delimiter).filter(Boolean);
  const extensions = process.platform === "win32" ? [".exe"] : [""];
  for (const directory of directories) {
    for (const extension of extensions) {
      const candidate = path.join(directory, `${name}${extension}`);
      if (fs.existsSync(candidate) && fs.statSync(candidate).isFile()) return candidate;
    }
  }
  return null;
}

function bundledElectronPath() {
  if (process.platform === "darwin") {
    return path.join(sourceAppDirectory, "node_modules", "electron", "dist", "Electron.app", "Contents", "MacOS", "Electron");
  }
  return path.join(
    sourceAppDirectory,
    "node_modules",
    "electron",
    "dist",
    process.platform === "win32" ? "electron.exe" : "electron",
  );
}

function resolveElectronPath() {
  const configured = process.env.WAZO_ELECTRON_PATH?.trim();
  if (configured) return path.resolve(configured);

  const bundled = bundledElectronPath();
  if (fs.existsSync(bundled)) return bundled;
  return findExecutableOnPath("electron") || bundled;
}

const sceneDirections = {
  "01-introduction": {
    title: "Meet WAZO",
    shots: [
      {
        at: 0,
        view: "portfolio",
        scrollFrom: 0,
        scrollTo: 0.12,
        cursor: [
          { at: 0, selector: ".brand" },
          { at: 0.34, selector: "#content .metric" },
          { at: 0.7, selector: "#content .panel" },
        ],
      },
    ],
  },
  "02-for-whom": {
    title: "Individuals & families",
    shots: [
      {
        at: 0,
        view: "help",
        scrollFrom: 0,
        scrollTo: { heading: "How the App Works", offset: 90 },
        cursor: [
          { at: 0, selector: "button[data-view='help']" },
          { at: 0.4, heading: "How the App Works" },
          { at: 0.78, selector: "#content .faq" },
        ],
      },
    ],
  },
  "03-family-ownership": {
    title: "Clear family ownership",
    shots: [
      {
        at: 0,
        view: "settings",
        settingsSection: "members",
        scrollFrom: 0,
        scrollTo: 0.38,
        cursor: [
          { at: 0, selector: "button[data-view='settings']" },
          { at: 0.2, selector: "button[data-section='members']" },
          { at: 0.54, selector: "#content .panel" },
          { at: 0.82, selector: "#content table" },
        ],
      },
    ],
  },
  "04-asset-library": {
    title: "Consistent asset records",
    shots: [
      {
        at: 0,
        view: "assetLibrary",
        scrollFrom: { heading: "Allocation Targets", offset: 90 },
        scrollTo: { heading: "Definition Library", offset: 90 },
        cursor: [
          { at: 0, selector: "button[data-view='assetLibrary']" },
          { at: 0.22, heading: "Allocation Targets" },
          { at: 0.58, heading: "Definition Library" },
          { at: 0.84, selector: "#asset-definitions-table" },
        ],
      },
    ],
  },
  "05-recurring-investments": {
    title: "Review recurring investments",
    shots: [
      {
        at: 0,
        view: "assets",
        scrollFrom: { heading: "Recurring Plans & Asset Transactions", offset: 90 },
        scrollTo: { heading: "Confirmed Asset Transactions", offset: 90 },
        cursor: [
          { at: 0, heading: "Recurring Plans & Asset Transactions" },
          { at: 0.38, heading: "Pending Investment Reviews" },
          { at: 0.76, heading: "Confirmed Asset Transactions" },
        ],
      },
    ],
  },
  "06-goals-performance": {
    title: "Goals & performance",
    shots: [
      {
        at: 0,
        view: "budget",
        scrollFrom: 0,
        scrollTo: 0.28,
        cursor: [
          { at: 0, selector: "button[data-view='budget']" },
          { at: 0.32, selector: "#content .metric" },
          { at: 0.7, selector: "#content .panel" },
        ],
      },
      {
        at: 0.48,
        view: "reports",
        scrollFrom: 0,
        scrollTo: 0.34,
        cursor: [
          { at: 0, selector: "button[data-view='reports']" },
          { at: 0.34, selector: "#content .metric" },
          { at: 0.7, selector: "#content .panel" },
        ],
      },
    ],
  },
  "07-reports-exports": {
    title: "Reports & exports",
    shots: [
      {
        at: 0,
        view: "reports",
        scrollFrom: { heading: "Export & Print Center", offset: 90 },
        scrollTo: { heading: "Reusable Export Presets", offset: 90 },
        cursor: [
          { at: 0, heading: "Export & Print Center" },
          { at: 0.4, selector: "#content .export-actions" },
          { at: 0.76, heading: "Reusable Export Presets" },
        ],
      },
    ],
  },
  "08-privacy-backups": {
    title: "Privacy & backups",
    shots: [
      {
        at: 0,
        view: "portfolio",
        privacy: true,
        scrollFrom: 0,
        scrollTo: 0.2,
        cursor: [
          { at: 0, selector: ".privacy-switch" },
          { at: 0.45, selector: "#content .metric" },
        ],
      },
      {
        at: 0.46,
        view: "settings",
        settingsSection: "storage",
        privacy: true,
        scrollFrom: { heading: "Backup Location", offset: 90 },
        scrollTo: { heading: "Automatic Backup", offset: 90 },
        cursor: [
          { at: 0, selector: "button[data-view='settings']" },
          { at: 0.2, selector: "button[data-section='storage']" },
          { at: 0.5, heading: "Backup Location" },
          { at: 0.78, heading: "Automatic Backup" },
        ],
      },
    ],
  },
  "09-optional-features": {
    title: "Optional rates & zakat",
    shots: [
      {
        at: 0,
        view: "settings",
        settingsSection: "general",
        privacy: false,
        scrollFrom: 0,
        scrollTo: { heading: "Online Rate Updates", offset: 90 },
        cursor: [
          { at: 0, selector: "button[data-section='general']" },
          { at: 0.45, heading: "Online Rate Updates" },
        ],
      },
      {
        at: 0.5,
        view: "zakat",
        scrollFrom: 0,
        scrollTo: 0.3,
        cursor: [
          { at: 0, selector: "button[data-view='zakat']" },
          { at: 0.4, selector: "#content .metric" },
          { at: 0.76, selector: "#content .panel" },
        ],
      },
    ],
  },
  "10-closing": {
    title: "Your wealth, clearly organized",
    shots: [
      { at: 0, view: "portfolio", scrollFrom: 0, scrollTo: 0.18, cursor: [{ at: 0, selector: "button[data-view='portfolio']" }, { at: 0.46, selector: "#content .metric" }] },
      { at: 0.25, view: "assets", scrollFrom: 0, scrollTo: 0.2, cursor: [{ at: 0, selector: "button[data-view='assets']" }, { at: 0.4, selector: "#content table" }] },
      { at: 0.45, view: "budget", scrollFrom: 0, scrollTo: 0.18, cursor: [{ at: 0, selector: "button[data-view='budget']" }, { at: 0.4, selector: "#content .panel" }] },
      { at: 0.63, view: "reports", scrollFrom: 0, scrollTo: 0.22, cursor: [{ at: 0, selector: "button[data-view='reports']" }, { at: 0.4, selector: "#content .metric" }] },
      { at: 0.81, view: "portfolio", scrollFrom: 0.18, scrollTo: 0, cursor: [{ at: 0, selector: ".brand" }, { at: 0.5, selector: "#content .metric" }] },
    ],
  },
};

function parseArguments(argv) {
  const options = { fps: DEFAULT_FPS, overwrite: false, smoke: false };
  for (let index = 0; index < argv.length; index += 1) {
    const argument = argv[index];
    if (argument === "--overwrite") options.overwrite = true;
    else if (argument === "--smoke") options.smoke = true;
    else if (argument === "--fps") {
      const value = Number(argv[index + 1]);
      if (!Number.isFinite(value) || value < 1 || value > 12) throw new Error("--fps must be between 1 and 12");
      options.fps = value;
      index += 1;
    } else if (argument === "--help" || argument === "-h") {
      console.log("Usage: node capture_walkthrough.js [--fps 6] [--overwrite] [--smoke]");
      process.exit(0);
    } else {
      throw new Error(`Unknown argument: ${argument}`);
    }
  }
  return options;
}

function delay(milliseconds) {
  return new Promise((resolve) => setTimeout(resolve, milliseconds));
}

function easeInOut(value) {
  const bounded = Math.max(0, Math.min(1, value));
  return bounded < 0.5 ? 2 * bounded * bounded : 1 - Math.pow(-2 * bounded + 2, 2) / 2;
}

function sha256(value) {
  return crypto.createHash("sha256").update(value).digest("hex").toUpperCase();
}

async function freePort() {
  return new Promise((resolve, reject) => {
    const server = net.createServer();
    server.unref();
    server.on("error", reject);
    server.listen(0, "127.0.0.1", () => {
      const { port } = server.address();
      server.close(() => resolve(port));
    });
  });
}

async function jsonRequest(url) {
  return new Promise((resolve, reject) => {
    const request = http.get(url, (response) => {
      let body = "";
      response.setEncoding("utf8");
      response.on("data", (chunk) => { body += chunk; });
      response.on("end", () => {
        if (response.statusCode < 200 || response.statusCode >= 300) {
          reject(new Error(`HTTP ${response.statusCode}: ${body}`));
          return;
        }
        try {
          resolve(JSON.parse(body));
        } catch (error) {
          reject(error);
        }
      });
    });
    request.on("error", reject);
    request.setTimeout(1000, () => request.destroy(new Error("DevTools request timed out")));
  });
}

async function waitForTarget(port, child) {
  const deadline = Date.now() + 30000;
  while (Date.now() < deadline) {
    if (child.exitCode !== null) throw new Error(`Electron exited before capture (code ${child.exitCode})`);
    try {
      const targets = await jsonRequest(`http://127.0.0.1:${port}/json/list`);
      const target = targets.find((item) => item.type === "page" && /renderer\/index\.html/i.test(item.url));
      if (target?.webSocketDebuggerUrl) return target;
    } catch {
      // Electron may still be starting.
    }
    await delay(150);
  }
  throw new Error("Timed out waiting for the WAZO renderer DevTools target");
}

class CdpClient {
  constructor(url) {
    this.url = url;
    this.nextId = 1;
    this.pending = new Map();
  }

  async connect() {
    this.socket = new WebSocket(this.url);
    await new Promise((resolve, reject) => {
      this.socket.addEventListener("open", resolve, { once: true });
      this.socket.addEventListener("error", reject, { once: true });
    });
    this.socket.addEventListener("message", (event) => {
      const message = JSON.parse(String(event.data));
      if (!message.id || !this.pending.has(message.id)) return;
      const { resolve, reject } = this.pending.get(message.id);
      this.pending.delete(message.id);
      if (message.error) reject(new Error(`${message.error.message}: ${message.error.data || ""}`));
      else resolve(message.result || {});
    });
  }

  call(method, params = {}) {
    const id = this.nextId;
    this.nextId += 1;
    return new Promise((resolve, reject) => {
      this.pending.set(id, { resolve, reject });
      this.socket.send(JSON.stringify({ id, method, params }));
    });
  }

  async evaluate(expression) {
    const result = await this.call("Runtime.evaluate", {
      expression,
      awaitPromise: true,
      returnByValue: true,
      userGesture: true,
    });
    if (result.exceptionDetails) {
      throw new Error(result.exceptionDetails.exception?.description || result.exceptionDetails.text || "Renderer evaluation failed");
    }
    return result.result?.value;
  }

  close() {
    if (this.socket?.readyState === WebSocket.OPEN) this.socket.close();
  }
}

function extractCaptureDataExpression() {
  const historicalHarness = fs.readFileSync(historicalHarnessPath, "utf8");
  const match = historicalHarness.match(/const captureDataExpression = `([\s\S]*?)`;\s*function viewExpression/);
  if (!match) throw new Error("Could not extract captureDataExpression from the v1.1.4 screenshot harness");
  return match[1];
}

function assertSourceCommit() {
  const revision = spawnSync("git", ["-C", sourceAppDirectory, "rev-parse", "HEAD"], {
    encoding: "utf8",
    windowsHide: true,
  });
  assert.equal(
    revision.status,
    0,
    `Could not verify the WAZO source commit at ${sourceAppDirectory}. Ensure it is a Git checkout and Git is on PATH. ${revision.stderr || revision.error || ""}`,
  );
  const actualCommit = revision.stdout.trim().toLowerCase();
  assert.equal(
    actualCommit,
    SOURCE_COMMIT,
    `WAZO source commit mismatch: expected ${SOURCE_COMMIT}, received ${actualCommit}. Check out the recorded commit before capture.`,
  );

  const status = spawnSync("git", ["-C", sourceAppDirectory, "status", "--porcelain", "--untracked-files=no"], {
    encoding: "utf8",
    windowsHide: true,
  });
  assert.equal(status.status, 0, `Could not inspect the WAZO source worktree. ${status.stderr || status.error || ""}`);
  assert.equal(
    status.stdout.trim(),
    "",
    "The WAZO source checkout has tracked changes. Use a clean checkout of the recorded commit before capture.",
  );
}

function assertInputs(timeline) {
  const packagePath = path.join(sourceAppDirectory, "package.json");
  assert.ok(
    fs.existsSync(packagePath),
    `WAZO v1.1.4 source checkout not found: ${sourceAppDirectory}. Set WAZO_APP_SOURCE to its directory.`,
  );
  assert.ok(
    fs.existsSync(historicalHarnessPath),
    `Historical capture harness not found: ${historicalHarnessPath}`,
  );
  assertSourceCommit();
  assert.equal(JSON.parse(fs.readFileSync(packagePath, "utf8")).version, "1.1.4");
  assert.ok(
    fs.existsSync(electronPath),
    `Electron executable not found: ${electronPath}. Set WAZO_ELECTRON_PATH or install Electron in the app checkout.`,
  );
  assert.ok(Array.isArray(timeline.scenes) && timeline.scenes.length === 10, "Expected ten narrated scenes");
  assert.ok(timeline.videoDuration > 120 && timeline.videoDuration < 123, "Unexpected narrated video duration");
  for (const scene of timeline.scenes) {
    const direction = sceneDirections[scene.id];
    assert.ok(direction, `No capture direction for ${scene.id}`);
    assert.ok(direction.shots.length > 0 && direction.shots[0].at === 0, `${scene.id} must start with a shot at zero`);
  }
}

function prepareOutput(overwrite) {
  fs.mkdirSync(framesDirectory, { recursive: true });
  fs.mkdirSync(path.dirname(manifestPath), { recursive: true });
  const existingFrames = fs.readdirSync(framesDirectory).filter((name) => /^frame-\d{6}\.jpg$/i.test(name));
  if (existingFrames.length && !overwrite) {
    throw new Error(`${existingFrames.length} capture frames already exist. Pass --overwrite to replace only frame-######.jpg files.`);
  }
  if (overwrite) {
    for (const name of existingFrames) fs.unlinkSync(path.join(framesDirectory, name));
  }
  const freeBytes = fs.statfsSync(framesDirectory).bavail * fs.statfsSync(framesDirectory).bsize;
  if (freeBytes < MINIMUM_FREE_BYTES) {
    throw new Error(`Only ${(freeBytes / 1024 / 1024).toFixed(0)} MB is free; at least ${MINIMUM_FREE_BYTES / 1024 / 1024} MB is required for capture.`);
  }
  return freeBytes;
}

const overlayExpression = `(() => {
  if (window.__wazoCapture) return true;
  const style = document.createElement("style");
  style.id = "wazo-capture-style";
  style.textContent = \`
    #wazo-capture-card {
      position: fixed;
      top: 88px;
      right: 38px;
      z-index: 2147483640;
      width: min(540px, calc(100vw - 360px));
      padding: 16px 20px 14px;
      border: 1px solid rgba(255, 255, 255, 0.72);
      border-radius: 20px;
      background: linear-gradient(135deg, rgba(37, 20, 77, 0.94), rgba(116, 55, 232, 0.9));
      box-shadow: 0 20px 55px rgba(43, 20, 89, 0.24);
      color: #fff;
      font-family: Inter, "Segoe UI", sans-serif;
      pointer-events: none;
      backdrop-filter: blur(18px);
    }
    #wazo-capture-kicker {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      margin-bottom: 5px;
      color: rgba(255, 255, 255, 0.72);
      font-size: 13px;
      font-weight: 800;
      letter-spacing: 0.14em;
      text-transform: uppercase;
    }
    #wazo-capture-title {
      font-size: 27px;
      font-weight: 780;
      letter-spacing: -0.02em;
      line-height: 1.15;
    }
    #wazo-capture-progress {
      height: 4px;
      margin-top: 12px;
      overflow: hidden;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.2);
    }
    #wazo-capture-progress > span {
      display: block;
      width: 0;
      height: 100%;
      border-radius: inherit;
      background: linear-gradient(90deg, #78efe1, #fff1a8);
    }
    #wazo-capture-cursor {
      position: fixed;
      left: 320px;
      top: 160px;
      z-index: 2147483646;
      width: 24px;
      height: 24px;
      border: 4px solid #fff;
      border-radius: 50%;
      background: #7437e8;
      box-shadow: 0 4px 18px rgba(38, 13, 82, 0.5), 0 0 0 7px rgba(116, 55, 232, 0.2);
      transform: translate(-50%, -50%);
      pointer-events: none;
    }
    #wazo-capture-cursor.pulse { box-shadow: 0 4px 18px rgba(38, 13, 82, 0.5), 0 0 0 16px rgba(116, 55, 232, 0.13); }
    body[data-view="settings"] #content .data-path,
    body[data-view="settings"] #content .danger-zone,
    body[data-view="settings"] #content [data-action="reveal-data"],
    body[data-view="settings"] #content [data-action="import-data"],
    body[data-view="settings"] #content [data-action="clear-backup-location"],
    body[data-view="settings"] #content [data-action="open-backup-location"],
    body[data-view="settings"] #content [data-action="choose-backup-location"] { display: none !important; }
  \`;
  document.head.appendChild(style);

  const card = document.createElement("div");
  card.id = "wazo-capture-card";
  card.setAttribute("aria-hidden", "true");
  card.innerHTML = \`<div id="wazo-capture-kicker"><span>WAZO WALKTHROUGH</span><span id="wazo-capture-scene"></span></div><div id="wazo-capture-title"></div><div id="wazo-capture-progress"><span></span></div>\`;
  document.body.appendChild(card);

  const cursor = document.createElement("div");
  cursor.id = "wazo-capture-cursor";
  cursor.setAttribute("aria-hidden", "true");
  document.body.appendChild(cursor);

  const centerOf = (target) => {
    let element = null;
    if (target?.selector) element = document.querySelector(target.selector);
    if (!element && target?.heading) {
      element = [...document.querySelectorAll("h2, h3, .panel-title")].find((candidate) => candidate.textContent.includes(target.heading));
    }
    if (!element) return null;
    const rect = element.getBoundingClientRect();
    return { x: rect.left + rect.width / 2, y: rect.top + Math.min(rect.height / 2, 44) };
  };

  window.__wazoCapture = {
    x: 320,
    y: 160,
    update(payload) {
      document.getElementById("wazo-capture-title").textContent = payload.title;
      document.getElementById("wazo-capture-scene").textContent = String(payload.scene).padStart(2, "0") + " / " + String(payload.total).padStart(2, "0");
      document.querySelector("#wazo-capture-progress > span").style.width = (Math.max(0, Math.min(1, payload.progress)) * 100).toFixed(2) + "%";
      const target = centerOf(payload.cursorTarget) || { x: 440, y: 220 };
      this.x += (target.x - this.x) * 0.22;
      this.y += (target.y - this.y) * 0.22;
      cursor.style.left = this.x.toFixed(2) + "px";
      cursor.style.top = this.y.toFixed(2) + "px";
      cursor.classList.toggle("pulse", Boolean(payload.pulse));
    }
  };
  return true;
})()`;

function resolveScene(timeline, time) {
  return timeline.scenes.find((scene) => time >= scene.start && time < scene.sceneEnd) || timeline.scenes[timeline.scenes.length - 1];
}

function resolveShot(direction, sceneProgress) {
  let index = 0;
  for (let candidate = 1; candidate < direction.shots.length; candidate += 1) {
    if (sceneProgress >= direction.shots[candidate].at) index = candidate;
    else break;
  }
  const shot = direction.shots[index];
  const end = direction.shots[index + 1]?.at ?? 1;
  const localProgress = Math.max(0, Math.min(1, (sceneProgress - shot.at) / Math.max(0.0001, end - shot.at)));
  return { shot, index, localProgress };
}

function resolveCursorTarget(shot, localProgress) {
  const targets = shot.cursor || [];
  let target = targets[0] || { selector: ".brand" };
  for (const candidate of targets) {
    if (localProgress >= candidate.at) target = candidate;
    else break;
  }
  return target.selector ? { selector: target.selector } : { heading: target.heading };
}

function activateShotExpression(shot) {
  return `(async () => {
    const requestedView = ${JSON.stringify(shot.view)};
    const navButton = document.querySelector('button[data-view="' + requestedView + '"]');
    if (!navButton) throw new Error('View is unavailable: ' + requestedView);
    navButton.click();
    ${shot.settingsSection ? `{
      const requestedSection = ${JSON.stringify(shot.settingsSection)};
      const sectionButton = document.querySelector('button[data-action="settings-section"][data-section="' + requestedSection + '"]');
      if (!sectionButton) throw new Error('Settings section is unavailable: ' + requestedSection);
      sectionButton.click();
      const sectionDeadline = Date.now() + 2000;
      while (ui.settingsSection !== requestedSection && Date.now() < sectionDeadline) {
        await new Promise((resolve) => setTimeout(resolve, 20));
      }
      if (ui.settingsSection !== requestedSection) throw new Error('Settings section did not activate: ' + requestedSection);
    }` : ""}
    ${typeof shot.privacy === "boolean" ? `state.settings.privacyLock = ${JSON.stringify(shot.privacy)}; applyUiPreferences(); renderShell(); renderView();` : ""}
    const content = document.getElementById("content");
    content.scrollTop = 0;
    await document.fonts.ready;
    await Promise.all([...document.images].map((image) => image.complete ? Promise.resolve() : new Promise((resolve) => {
      image.addEventListener("load", resolve, { once: true });
      image.addEventListener("error", resolve, { once: true });
    })));
    await new Promise((resolve) => requestAnimationFrame(() => requestAnimationFrame(resolve)));

    const resolveScroll = (specification) => {
      const maximum = Math.max(0, content.scrollHeight - content.clientHeight);
      if (typeof specification === "number") return Math.max(0, Math.min(maximum, maximum * specification));
      if (specification?.heading) {
        const heading = [...content.querySelectorAll("h2, h3, .panel-title")].find((item) => item.textContent.includes(specification.heading));
        return heading ? Math.max(0, Math.min(maximum, heading.closest("section, .backup-box, .panel")?.offsetTop - (specification.offset || 80))) : maximum * 0.5;
      }
      return 0;
    };

    const visibleText = document.body.innerText || "";
    const personalPathPattern = /(?:[A-Z]:\\\\Users\\\\|OneDrive\\s*-\\s*TRADER|Zubair\\.Shaikh)/i;
    if (personalPathPattern.test(visibleText)) throw new Error("A personal local path is visible in the capture view");
    return {
      requestedView,
      actualView: document.body.dataset.view,
      pageTitle: document.getElementById("page-title")?.textContent || "",
      scrollFrom: resolveScroll(${JSON.stringify(shot.scrollFrom ?? 0)}),
      scrollTo: resolveScroll(${JSON.stringify(shot.scrollTo ?? 0)}),
      scrollMaximum: Math.max(0, content.scrollHeight - content.clientHeight),
      privacyActive: document.querySelector(".privacy-switch")?.classList.contains("active") || false,
      logoLoaded: document.querySelector(".brand-logo")?.complete || false
    };
  })()`;
}

function updateFrameExpression(payload) {
  return `(() => {
    const content = document.getElementById("content");
    content.scrollTop = ${JSON.stringify(payload.scrollTop)};
    window.__wazoCapture.update(${JSON.stringify(payload.overlay)});
    return { scrollTop: content.scrollTop, view: document.body.dataset.view };
  })()`;
}

function frameName(index) {
  return `frame-${String(index + 1).padStart(6, "0")}.jpg`;
}

async function captureJpeg(cdp) {
  const result = await cdp.call("Page.captureScreenshot", {
    format: "jpeg",
    quality: JPEG_QUALITY,
    fromSurface: true,
    captureBeyondViewport: false,
  });
  const buffer = Buffer.from(result.data, "base64");
  assert.equal(buffer[0], 0xff, "JPEG start marker byte 1");
  assert.equal(buffer[1], 0xd8, "JPEG start marker byte 2");
  assert.ok(buffer.length > 30 * 1024, "Captured JPEG is unexpectedly small");
  return buffer;
}

async function closeElectron(child, cdp) {
  await cdp?.call("Browser.close").catch(() => {});
  await new Promise((resolve) => {
    if (!child || child.exitCode !== null) {
      resolve();
      return;
    }
    const timer = setTimeout(resolve, 5000);
    child.once("exit", () => {
      clearTimeout(timer);
      resolve();
    });
  });
  if (child?.exitCode === null) child.kill();
}

async function run() {
  const options = parseArguments(process.argv.slice(2));
  const timeline = JSON.parse(fs.readFileSync(timelinePath, "utf8"));
  assertInputs(timeline);
  const captureDataExpression = extractCaptureDataExpression();
  const freeBytesBefore = options.smoke ? null : prepareOutput(options.overwrite);
  const profileDirectory = fs.mkdtempSync(path.join(os.tmpdir(), "wazo-narrated-capture-v114-"));
  const port = await freePort();
  let child;
  let cdp;
  let stderr = "";

  try {
    child = spawn(electronPath, [
      `--remote-debugging-port=${port}`,
      `--user-data-dir=${profileDirectory}`,
      "--no-first-run",
      sourceAppDirectory,
    ], {
      cwd: sourceAppDirectory,
      stdio: ["ignore", "pipe", "pipe"],
      windowsHide: true,
    });
    child.stderr.on("data", (chunk) => { stderr += chunk.toString(); });

    const target = await waitForTarget(port, child);
    cdp = new CdpClient(target.webSocketDebuggerUrl);
    await cdp.connect();
    await cdp.call("Page.enable");
    await cdp.call("Runtime.enable");
    await cdp.call("Emulation.setDeviceMetricsOverride", {
      width: viewport.cssWidth,
      height: viewport.cssHeight,
      deviceScaleFactor: viewport.deviceScaleFactor,
      mobile: false,
      screenWidth: viewport.cssWidth,
      screenHeight: viewport.cssHeight,
      screenOrientation: { type: "landscapePrimary", angle: 0 },
    });

    await cdp.evaluate(`new Promise((resolve, reject) => {
      const deadline = Date.now() + 20000;
      const timer = setInterval(() => {
        if (typeof state !== "undefined" && state && document.getElementById("content")) {
          clearInterval(timer);
          resolve(true);
        } else if (Date.now() > deadline) {
          clearInterval(timer);
          reject(new Error("WAZO renderer did not initialize"));
        }
      }, 100);
    })`);

    const captureState = await cdp.evaluate(captureDataExpression);
    assert.equal(captureState.profile, "Demo Family");
    assert.equal(captureState.privacyMode, false);
    assert.equal(captureState.plans, 1);
    assert.equal(captureState.transactions, 2);
    await cdp.evaluate(overlayExpression);

    if (options.smoke) {
      let smokeBytes = 0;
      let smokeShots = 0;
      for (const scene of timeline.scenes) {
        const direction = sceneDirections[scene.id];
        for (const shot of direction.shots) {
          const shotState = await cdp.evaluate(activateShotExpression(shot));
          assert.equal(shotState.actualView, shot.view, `${scene.id} smoke view`);
          assert.equal(shotState.logoLoaded, true, `${scene.id} smoke logo`);
          if (typeof shot.privacy === "boolean") assert.equal(shotState.privacyActive, shot.privacy, `${scene.id} smoke privacy`);
          await cdp.evaluate(updateFrameExpression({
            scrollTop: shotState.scrollFrom + (shotState.scrollTo - shotState.scrollFrom) * 0.5,
            overlay: {
              title: direction.title,
              scene: scene.index,
              total: timeline.scenes.length,
              progress: 0.5,
              cursorTarget: resolveCursorTarget(shot, 0.5),
              pulse: false,
            },
          }));
          const buffer = await captureJpeg(cdp);
          smokeBytes += buffer.length;
          smokeShots += 1;
        }
      }
      console.log(`Smoke capture passed for ${smokeShots} live shots (${(smokeBytes / 1024).toFixed(0)} KB checked in memory; no frames written).`);
      await closeElectron(child, cdp);
      return;
    }

    const frameCount = Math.ceil(timeline.videoDuration * options.fps);
    const captureDigest = crypto.createHash("sha256");
    let totalBytes = 0;
    let activeKey = "";
    let activeShotState = null;
    const startedAt = new Date();

    for (let frameIndex = 0; frameIndex < frameCount; frameIndex += 1) {
      const time = Math.min(frameIndex / options.fps, timeline.videoDuration - 0.001);
      const scene = resolveScene(timeline, time);
      const direction = sceneDirections[scene.id];
      const sceneProgress = Math.max(0, Math.min(1, (time - scene.start) / Math.max(0.001, scene.sceneEnd - scene.start)));
      const resolved = resolveShot(direction, sceneProgress);
      const key = `${scene.id}:${resolved.index}`;

      if (key !== activeKey) {
        activeShotState = await cdp.evaluate(activateShotExpression(resolved.shot));
        assert.equal(activeShotState.actualView, resolved.shot.view, `${key} view`);
        assert.equal(activeShotState.logoLoaded, true, `${key} logo`);
        if (typeof resolved.shot.privacy === "boolean") assert.equal(activeShotState.privacyActive, resolved.shot.privacy, `${key} privacy state`);
        activeKey = key;
      }

      const scrollProgress = easeInOut(resolved.localProgress);
      const scrollTop = activeShotState.scrollFrom + (activeShotState.scrollTo - activeShotState.scrollFrom) * scrollProgress;
      await cdp.evaluate(updateFrameExpression({
        scrollTop,
        overlay: {
          title: direction.title,
          scene: scene.index,
          total: timeline.scenes.length,
          progress: sceneProgress,
          cursorTarget: resolveCursorTarget(resolved.shot, resolved.localProgress),
          pulse: resolved.localProgress < 0.075,
        },
      }));

      const buffer = await captureJpeg(cdp);
      fs.writeFileSync(path.join(framesDirectory, frameName(frameIndex)), buffer);
      captureDigest.update(buffer);
      totalBytes += buffer.length;
      if ((frameIndex + 1) % 30 === 0 || frameIndex + 1 === frameCount) {
        console.log(`Captured ${frameIndex + 1}/${frameCount} frames (${(totalBytes / 1024 / 1024).toFixed(1)} MB).`);
      }
    }

    const endedAt = new Date();
    const freeBytesAfter = fs.statfsSync(framesDirectory).bavail * fs.statfsSync(framesDirectory).bsize;
    const manifest = {
      title: "WAZO v1.1.4 narrated explainer — live app capture",
      generatedAt: endedAt.toISOString(),
      source: {
        version: "1.1.4",
        commit: SOURCE_COMMIT,
        commitVerified: true,
        app: "source-app-v1.1.4",
        historicalCaptureHarness: "source-app-v1.1.4/scripts/capture-store-screenshots.js",
        captureDataExpressionSha256: sha256(captureDataExpression),
      },
      capture: {
        fps: options.fps,
        frameCount,
        timelineDurationSeconds: timeline.videoDuration,
        encodedFrameDurationSeconds: frameCount / options.fps,
        outputPattern: "capture-frames/frame-%06d.jpg",
        format: "JPEG",
        jpegQuality: JPEG_QUALITY,
        viewport: {
          css: `${viewport.cssWidth}x${viewport.cssHeight}`,
          deviceScaleFactor: viewport.deviceScaleFactor,
          output: `${viewport.outputWidth}x${viewport.outputHeight}`,
        },
        bytes: totalBytes,
        megabytes: Number((totalBytes / 1024 / 1024).toFixed(2)),
        concatenatedFrameSha256: captureDigest.digest("hex").toUpperCase(),
        startedAt: startedAt.toISOString(),
        completedAt: endedAt.toISOString(),
      },
      data: {
        profile: "fresh isolated Electron user-data directory",
        content: "bundled anonymous demo data plus one in-memory capture-only SIP example",
        installedUserDataUsed: false,
        repositorySeedModified: false,
      },
      safety: {
        visiblePersonalPathScan: "passed for every activated shot",
        settingsStoragePaths: "hidden with capture-only CSS",
        dialogsOpened: false,
        destructiveActionsInvoked: false,
        persistentAppSettingsChanged: false,
      },
      storage: {
        freeBytesBefore,
        freeBytesAfter,
        estimatedCaptureBytes: ESTIMATED_CAPTURE_BYTES,
      },
      scenes: timeline.scenes.map((scene) => ({
        index: scene.index,
        id: scene.id,
        start: scene.start,
        end: scene.sceneEnd,
        overlayTitle: sceneDirections[scene.id].title,
        shots: sceneDirections[scene.id].shots.map((shot) => ({
          at: shot.at,
          view: shot.view,
          ...(shot.settingsSection ? { settingsSection: shot.settingsSection } : {}),
          ...(typeof shot.privacy === "boolean" ? { privacy: shot.privacy } : {}),
        })),
      })),
    };
    fs.writeFileSync(manifestPath, `${JSON.stringify(manifest, null, 2)}\n`);
    await closeElectron(child, cdp);

    if (stderr && /Startup Failed/i.test(stderr)) throw new Error(stderr.trim());
    console.log(`Live WAZO capture complete: ${frameCount} frames, ${(totalBytes / 1024 / 1024).toFixed(1)} MB.`);
  } finally {
    cdp?.close();
    if (child?.exitCode === null) child.kill();
    fs.rmSync(profileDirectory, { recursive: true, force: true, maxRetries: 5, retryDelay: 150 });
  }
}

run().catch((error) => {
  console.error(error.stack || error.message);
  process.exitCode = 1;
});

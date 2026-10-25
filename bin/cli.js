#!/usr/bin/env node
const fs = require("fs");
const path = require("path");
const { execSync, spawn } = require("child_process");

const args = process.argv.slice(2);

function showHelp() {
  console.log(`
🎨 UI/UX Ultra v1.0.0 — 200 Curated Palettes, UX Laws & Multi-Platform Theme Compiler
   Crafted with ❤️ by Pardeep Kumar | Powered by ToolNPlay.com (https://ToolNPlay.com)
   GitHub: https://github.com/PardeepPatel/ui-ux-ultra

Usage:
  npx ui-ux-ultra [options]

Options:
  --global, -g     Install globally to ~/.gemini/antigravity/skills/ui-ux-ultra
  --cursor         Install to .cursor/skills/ui-ux-ultra
  --claude         Install to .claude/skills/ui-ux-ultra
  --gemini         Install to .gemini/skills/ui-ux-ultra
  --agents         Install to .agents/skills/ui-ux-ultra (default workspace install)
  --preview, -p    Launch interactive 200-Palette Studio Previewer in browser
  --export         Export all 200 palettes to JSON and CSV in skill/data
  --audit          Output real-time WCAG 2.1 contrast telemetry for palettes
  --help, -h       Show this help message

Search & Compilation:
  Pass keywords or python engine flags directly:
  npx ui-ux-ultra "travel saas" --category travel --persist --audit
`);
}

if (args.includes("--help") || args.includes("-h")) {
  showHelp();
  process.exit(0);
}

if (args.includes("--preview") || args.includes("-p")) {
  const previewPath = path.join(__dirname, "..", "previewer", "index.html");
  console.log(`\n🚀 Opening UI/UX Ultra Studio Previewer...`);
  console.log(`   File: ${previewPath}\n`);
  const openCmd = process.platform === "darwin" ? "open" : process.platform === "win32" ? "start" : "xdg-open";
  try {
    execSync(`${openCmd} "${previewPath}"`);
  } catch (err) {
    console.error(`Could not open browser automatically: ${err.message}`);
    console.log(`Please open: file://${previewPath}`);
  }
  process.exit(0);
}

if (args.includes("--export")) {
  const scriptPath = path.join(__dirname, "..", "skill", "scripts", "design_engine.py");
  try {
    execSync(`python3 "${scriptPath}" --export-catalog`, { stdio: "inherit" });
  } catch (err) {
    console.error(`Export failed: ${err.message}`);
    process.exit(1);
  }
  process.exit(0);
}

// Check if user is invoking the search or persist engine directly
const hasEngineFlags = args.some(a => ["--category", "--mode", "--palette-id", "--persist", "-p"].includes(a)) ||
  (args.length > 0 && !args[0].startsWith("-"));

if (hasEngineFlags && !args.includes("--global") && !args.includes("-g") && !args.includes("--cursor") && !args.includes("--claude")) {
  const scriptPath = path.join(__dirname, "..", "skill", "scripts", "design_engine.py");
  const child = spawn("python3", [scriptPath, ...args], { stdio: "inherit" });
  child.on("exit", code => process.exit(code || 0));
} else {
  // Installation mode
  const homeDir = process.env.HOME || process.env.USERPROFILE;
  const targets = [];

  if (args.includes("--global") || args.includes("-g")) {
    // Official Antigravity global custom skill discovery paths
    targets.push(path.join(homeDir, ".gemini", "config", "skills", "ui-ux-ultra"));
    targets.push(path.join(homeDir, ".gemini", "antigravity", "skills", "ui-ux-ultra"));
  } else if (args.includes("--cursor")) {
    targets.push(path.join(process.cwd(), ".cursor", "skills", "ui-ux-ultra"));
  } else if (args.includes("--claude")) {
    targets.push(path.join(process.cwd(), ".claude", "skills", "ui-ux-ultra"));
  } else if (args.includes("--gemini")) {
    targets.push(path.join(process.cwd(), ".agents", "skills", "ui-ux-ultra"));
    targets.push(path.join(homeDir, ".gemini", "config", "skills", "ui-ux-ultra"));
  } else {
    // Default workspace install (.agents/skills/ for Antigravity, Cursor & Claude)
    targets.push(path.join(process.cwd(), ".agents", "skills", "ui-ux-ultra"));
  }

  const sourceSkill = path.join(__dirname, "..", "skill");

  for (const targetBase of targets) {
    fs.mkdirSync(targetBase, { recursive: true });
    fs.cpSync(sourceSkill, targetBase, { recursive: true });
    console.log(`\n✅ UI/UX Ultra v1.0.0 (by ToolNPlay.com & Pardeep Kumar) installed to:`);
    console.log(`   ${targetBase}`);
  }
  console.log(`\n🎉 Skill is ready! In Antigravity, simply ask: "Build a SaaS app using ui-ux-ultra"\n`);
}

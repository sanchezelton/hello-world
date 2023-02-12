import "./style.css";
import * as THREE from "three";
import gsap from "gsap";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls";

document.querySelector<HTMLDivElement>("#app")!.innerHTML = `
  <canvas class="webgl"></canvas>
  <nav>
    <a href="/">Sphere</a>
    <ul>
      <li>Explore</li>
      <li>Create</li>
    </ul>
  </nav>
  <h1 class="title">Give it a spin</h1>
  `;

const scene = new THREE.Scene();

// create our sphere
const RADIUS = 3;
const SEGMENT_HEIGHT = 64;
const SEGMENT_WIDTH = 65;
const geometry = new THREE.SphereGeometry(
  RADIUS,
  SEGMENT_WIDTH,
  SEGMENT_HEIGHT
);
const material = new THREE.MeshStandardMaterial({
  color: "#00ff83",
});
const mesh = new THREE.Mesh(geometry, material);

// sizes
const sizes = {
  width: window.innerWidth,
  height: window.innerHeight,
};

// camera
const FOV = 35;
const NEAR_CLIP = 0.1;
const FAR_CLIP = 100;
const camera = new THREE.PerspectiveCamera(
  FOV,
  sizes.width / sizes.height,
  NEAR_CLIP,
  FAR_CLIP
);
camera.position.z = 20;

// light
const light = new THREE.PointLight(0xfffff, 1, 100);
light.position.set(0, 10, 10);

// add to scene
scene.add(light);
scene.add(camera);
scene.add(mesh);

// renderer
const canvas = document.querySelector<HTMLCanvasElement>(
  ".webgl"
) as HTMLCanvasElement;
const renderer = new THREE.WebGLRenderer({ canvas });
renderer.setSize(sizes.width, sizes.height);
renderer.setPixelRatio(2);
renderer.render(scene, camera);

// controls
const controls = new OrbitControls(camera, canvas);
controls.enableDamping = true;
controls.enablePan = false;
controls.enableZoom = false;
controls.autoRotate = true;

// resize
window.addEventListener("resize", () => {
  // update sizes
  sizes.width = window.innerWidth;
  sizes.height = window.innerHeight;
  // update camera
  camera.aspect = sizes.width / sizes.height;
  camera.updateProjectionMatrix();
  // update renderer
  renderer.setSize(sizes.width, sizes.height);
});

// mouse animation color
let mouseDown = false
let rgb = []
window.addEventListener("mousedown", () => mouseDown = true)
window.addEventListener("mouseup", () => mouseDown = false)
window.addEventListener("mousedown", (e) => {
  if (mouseDown && e.button > 0) {
    rgb = [
      Math.round((e.pageX / sizes.width) * 255),
      Math.round((e.pageY / sizes.height) * 255),
      150,
    ]
    // animate
    let newColor = new THREE.Color(`rgb(${rgb.join(',')})`)
    gsap.to(mesh.material.color, { r: newColor.r, g: newColor.g, b: newColor.b })
  }
})

const loop = () => {
  controls.update();
  renderer.render(scene, camera);
  window.requestAnimationFrame(loop);
};

loop();

// timeline magic
const t1 = gsap.timeline({ defaults: { duration: 1 } })
t1.fromTo(mesh.scale, { z: 0, y: 0, x: 0 }, { z: 1, y: 1, x: 1 })
t1.fromTo('nav', { y: '-100%'}, { y: "0%"})
t1.fromTo('.title', { opacity: 0 }, { opacity: 1})

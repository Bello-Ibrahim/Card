import {
  Activity,
  ArrowRightLeft,
  Boxes,
  Cloud,
  Compass,
  Database,
  GitBranch,
  Handshake,
  LineChart,
  Layers,
  Network,
  Rocket,
  ServerCog,
  ShieldCheck,
  Target,
  Users,
  Workflow,
  type LucideIcon,
} from "lucide-react";

const registry = {
  pipeline: Workflow,
  architecture: Layers,
  cloud: Cloud,
  warehouse: Database,
  integration: Network,
  migration: ArrowRightLeft,
  analytics: LineChart,
  quality: ShieldCheck,
  strategy: Compass,
  engineering: ServerCog,
  business: Target,
  production: Activity,
  transfer: Users,
  partnership: Handshake,
  scale: Rocket,
  build: Boxes,
  branch: GitBranch,
} as const;

export type IconName = keyof typeof registry;

export function Icon({
  name,
  className,
  strokeWidth = 1.5,
}: {
  name: IconName;
  className?: string;
  strokeWidth?: number;
}) {
  const Component: LucideIcon = registry[name];
  return <Component aria-hidden="true" className={className} strokeWidth={strokeWidth} />;
}


import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Progress } from "@/components/ui/progress";
import { ArrowUp, ArrowDown, Mail, Star, Calendar } from "lucide-react";

const SuccessMetrics = () => {
  // Mock data - would come from calculations in a real app
  const metrics = [
    {
      name: "Response Rate",
      value: 32,
      change: 8,
      trend: "up",
      icon: Mail,
    },
    {
      name: "Interview Rate",
      value: 18,
      change: 5,
      trend: "up",
      icon: Calendar,
    },
    {
      name: "Skills Match Average",
      value: 76,
      change: -4,
      trend: "down",
      icon: Star,
    },
    {
      name: "Application Quality",
      value: 85,
      change: 12,
      trend: "up",
      icon: ArrowUp,
    },
  ];

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-6">
      {metrics.map((metric) => (
        <Card key={metric.name} className="shadow-sm hover:shadow-md transition-shadow">
          <CardHeader className="pb-2">
            <div className="flex justify-between items-center">
              <CardTitle className="text-sm font-medium text-gray-500">{metric.name}</CardTitle>
              <metric.icon className="h-4 w-4 text-gray-400" />
            </div>
          </CardHeader>
          <CardContent>
            <div className="flex items-baseline justify-between">
              <div className="text-2xl font-bold">{metric.value}%</div>
              <div className={`flex items-center text-xs ${
                metric.trend === 'up' 
                  ? 'text-green-600' 
                  : 'text-red-600'
              }`}>
                {metric.trend === 'up' ? (
                  <ArrowUp className="h-3 w-3 mr-1" />
                ) : (
                  <ArrowDown className="h-3 w-3 mr-1" />
                )}
                {Math.abs(metric.change)}%
              </div>
            </div>
            <Progress 
              value={metric.value} 
              className={`h-1 mt-2 ${
                metric.trend === 'up' 
                  ? 'bg-green-100 text-green-500' 
                  : 'bg-red-100 text-red-500'
              }`} 
            />
          </CardContent>
        </Card>
      ))}
    </div>
  );
};

export default SuccessMetrics;

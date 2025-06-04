
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Check, Star } from "lucide-react";

const SuccessFactors = () => {
  const factors = [
    {
      id: 1,
      title: "Algorithm Selection",
      description: "Choosing the right approach for problem-solving",
      rating: 5,
      importance: "Critical for technical interviews",
    },
    {
      id: 2,
      title: "Implementation Quality",
      description: "Clean code with proper libraries and practices",
      rating: 4,
      importance: "Shows professional coding standards",
    },
    {
      id: 3,
      title: "Documentation",
      description: "Clear explanation of decisions and approaches",
      rating: 4,
      importance: "Demonstrates communication skills",
    },
    {
      id: 4,
      title: "Effectiveness Metrics",
      description: "Measuring and optimizing performance",
      rating: 3,
      importance: "Proves analytical thinking",
    },
    {
      id: 5,
      title: "Feature Selection",
      description: "Choosing the right features for implementation",
      rating: 4,
      importance: "Shows product thinking",
    },
    {
      id: 6,
      title: "Web Integration",
      description: "Seamless integration with web technologies",
      rating: 3,
      importance: "Demonstrates full-stack abilities",
    },
  ];

  return (
    <Card className="shadow-md">
      <CardHeader>
        <CardTitle className="text-xl text-primary">Key Success Factors</CardTitle>
        <CardDescription>
          Focus on these areas to improve your job application success
        </CardDescription>
      </CardHeader>
      <CardContent>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {factors.map((factor) => (
            <div key={factor.id} className="success-factor">
              <div className="flex justify-between items-start mb-2">
                <h3 className="font-semibold text-gray-800">{factor.title}</h3>
                <div className="flex">
                  {Array.from({ length: factor.rating }).map((_, i) => (
                    <Star key={i} className="h-4 w-4 fill-yellow-400 text-yellow-400" />
                  ))}
                </div>
              </div>
              <p className="text-sm text-gray-600 mb-2">{factor.description}</p>
              <div className="flex items-center text-xs text-primary">
                <Check className="h-3 w-3 mr-1" />
                <span>{factor.importance}</span>
              </div>
            </div>
          ))}
        </div>
      </CardContent>
    </Card>
  );
};

export default SuccessFactors;

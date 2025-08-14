#!/usr/bin/env python3
"""
Simple test script to verify backend functionality
"""

import sys
import os

# Add current directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test if all required modules can be imported"""
    try:
        from common import generator_llm, feedback_llm, extract_resume_text
        print("✅ Common module imports successful")
        
        from models import InterviewState, InterviewQuestions, StructuredEvaluator, FeedbackItem
        print("✅ Models module imports successful")
        
        from generator import generate_question
        print("✅ Generator module imports successful")
        
        from feedback import feedback_generator
        print("✅ Feedback module imports successful")
        
        from roadmap import generate_roadmap
        print("✅ Roadmap module imports successful")
        
        from workflow import workflow
        print("✅ Workflow module imports successful")
        
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def test_models():
    """Test if models can be instantiated"""
    try:
        from models import InterviewState, InterviewQuestions, StructuredEvaluator, FeedbackItem
        
        # Test InterviewQuestions
        questions = InterviewQuestions(questions=["Test question 1", "Test question 2", "Test question 3"])
        print("✅ InterviewQuestions model works")
        
        # Test FeedbackItem
        feedback = FeedbackItem(feedback="Test feedback", marks=8)
        print("✅ FeedbackItem model works")
        
        # Test StructuredEvaluator
        evaluator = StructuredEvaluator(feedback_list=[feedback])
        print("✅ StructuredEvaluator model works")
        
        return True
    except Exception as e:
        print(f"❌ Model test error: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Testing AI Interviewer Backend...")
    print("=" * 50)
    
    # Test imports
    if not test_imports():
        print("\n❌ Import tests failed. Please check your dependencies.")
        return False
    
    # Test models
    if not test_models():
        print("\n❌ Model tests failed. Please check your model definitions.")
        return False
    
    print("\n" + "=" * 50)
    print("🎉 All tests passed! Backend is ready.")
    print("\nTo start the backend server, run:")
    print("  cd backend")
    print("  ./start.sh")
    print("\nOr to start both frontend and backend:")
    print("  ./start.sh")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

---
layout: post
title: objc_getAssociatedObject
---
```objc
- (NSString *)assetID {

    NSString* origAssetID = objc_getAssociatedObject(self, @selector(assetID));

    if (origAssetID == nil) {
        if ([self isKindOfClass:[ESUPhoto class]]) {
            return nil;
        } else if ([self isKindOfClass:[ESUVideo class]]) {
            NSString *videoURL = ((ESUVideo *) self).videoURL;
            if (videoURL != nil) {
                objc_setAssociatedObject(self, @selector(assetID), [videoURL getAssetIdFromPath], OBJC_ASSOCIATION_RETAIN_NONATOMIC);
                self.modified = YES;
            } else {
                NSString *videoPath = ((ESUVideo *) self).videoPath;
                if (videoPath != nil) {

                    objc_setAssociatedObject(self, @selector(assetID), [videoPath getAssetIdFromPath], OBJC_ASSOCIATION_RETAIN_NONATOMIC);
                    self.modified = YES;
                }
            }
        }
    }

    return origAssetID;
}
```
